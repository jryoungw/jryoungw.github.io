'''Train CIFAR10 with PyTorch.'''
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import torch.backends.cudnn as cudnn

import torchvision
import torchvision.transforms as transforms

import os

os.environ["CUDA_DEVICE_ORDER"]="PCI_BUS_ID"   
os.environ["CUDA_VISIBLE_DEVICES"]='4'

import argparse
import numpy as np
from copy import deepcopy

from models import *
from utils import progress_bar


parser = argparse.ArgumentParser(description='PyTorch CIFAR10 Training')
parser.add_argument('--lr', default=0.1, type=float, help='learning rate')
parser.add_argument('--resume', '-r', action='store_true',
                    help='resume from checkpoint')
args = parser.parse_args()

device = 'cuda' if torch.cuda.is_available() else 'cpu'
best_acc = 0  # best test accuracy
start_epoch = 0  # start from epoch 0 or last checkpoint epoch

# Data
print('==> Preparing data..')
transform_train = transforms.Compose([
    transforms.RandomCrop(32, padding=4),
    transforms.RandomHorizontalFlip(),
    transforms.ToTensor(),
    transforms.Normalize((0.4914, 0.4822, 0.4465), (0.2023, 0.1994, 0.2010)),
])

transform_test = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.4914, 0.4822, 0.4465), (0.2023, 0.1994, 0.2010)),
])

bs = 128

trainset = torchvision.datasets.CIFAR10(
    root='./data', train=True, download=True, transform=transform_train)
trainloader = torch.utils.data.DataLoader(
    trainset, batch_size=bs, shuffle=True, num_workers=2)

testset = torchvision.datasets.CIFAR10(
    root='./data', train=False, download=True, transform=transform_test)
testloader = torch.utils.data.DataLoader(
    testset, batch_size=100, shuffle=False, num_workers=2)

classes = ('plane', 'car', 'bird', 'cat', 'deer',
           'dog', 'frog', 'horse', 'ship', 'truck')

# Model
print('==> Building model..')
# net = VGG('VGG19')
net = ResNet18()
# net = PreActResNet18()
# net = GoogLeNet()
# net = DenseNet121()
# net = ResNeXt29_2x64d()
# net = MobileNet()
# net = MobileNetV2()
# net = DPN92()
# net = ShuffleNetG2()
# net = SENet18()
# net = ShuffleNetV2(1)
# net = EfficientNetB0()
# net = RegNetX_200MF()
# net = SimpleDLA()
net = net.to(device)
# if device == 'cuda':
#     net = torch.nn.DataParallel(net)
#     cudnn.benchmark = True

if args.resume:
    # Load checkpoint.
    print('==> Resuming from checkpoint..')
    assert os.path.isdir('checkpoint'), 'Error: no checkpoint directory found!'
    checkpoint = torch.load('./checkpoint/ckpt.pth')
    net.load_state_dict(checkpoint['net'])
    best_acc = checkpoint['acc']
    start_epoch = checkpoint['epoch']

criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(net.parameters(), lr=args.lr,
                      momentum=0.9, weight_decay=5e-4)

def LALR7(base_lr, batch_length, loss_t, loss_t_1, org_params, new_params, grads=None, first=False, v=None, device='cuda', epoch=0):
    with torch.no_grad():
        loss_diff = loss_t_1 - loss_t
        param_diff = 0
        assert len(org_params) == len(new_params)
        if grads is not None:
            assert len(grads) == len(org_params)
        param_n = 0
        group_n = 0
        for idx, p in enumerate(org_params):
            param_diff = param_diff + torch.sum((p - new_params[idx])**2)
            group_n += 1
            param_n += p.numel()
        param_diff /= param_n
        if first:
            # v = [(new_params[i] - org_params[i]) + (base_lr * grads[i]) for i in range(len(grads))]
            v = [torch.randn(p.size()).to(device) * np.exp(-0.2 * epoch) for p in new_params]
            # v = [torch.randn(p.size()).to(device) for p in new_params]
        inner = torch.sum(torch.Tensor([torch.sum((v[i] / torch.std(new_params[i] - org_params[i]) + new_params[i] - org_params[i])\
                            * (new_params[i] - org_params[i])) for i in range(len(v))])) / param_n
        # inner = torch.sum(torch.Tensor([torch.sum(((v[i]) * torch.std(new_params[i] - org_params[i]) - new_params[i])\
                            # * (new_params[i] - org_params[i])) for i in range(len(v))])) / param_n
        new_lr = ((inner - param_diff) / loss_diff)# * np.exp(-0.1*epoch)
        print(inner.item(), param_diff.item(), loss_diff)
        # print(new_lr)
        if first:
            return torch.abs(new_lr), v
            # return new_lr, v
        return torch.abs(new_lr)
        # return new_lr

def LALR2(base_lr, grads, old_param, new_param, dt=1e-5):
    normsq = 0
    inner = 0
    loss_grad = []
    num_params = 0
    for i in range(len(old_param)):
        normsq += torch.sum((old_param[i] - new_param[i])**2)
        num_params += 1
    normsq /= num_params
    for p in grads:
        loss_grad.append(deepcopy(p))
    assert len(loss_grad) == len(old_param)
    for i in range(len(loss_grad)):
        inner += torch.sum(loss_grad[i])
    
    # if base_lr - normsq / inner < 0:
    #     return base_lr
    
    return max(torch.abs(base_lr - normsq / inner), dt)
    # return max(torch.abs(normsq / inner), dt)

def LALR3(base_lr, loss_diff, old_param, new_param, dt=1e-5):
    normsq = 0
    inner = 0
    loss_grad = []
    num_param = 0
    for i in range(len(old_param)):
        normsq += torch.sum((old_param[i] - new_param[i])**2)
        num_param += 1
    normsq /= num_param
    print(normsq)
    
    return max(torch.abs(base_lr - normsq / loss_diff), dt)


# Training
def train(epoch, loss_t_1, lr_, first, final_lrs, total_loss, v=None):
    lr = lr_
    print('\nEpoch: %d' % epoch)
    train_loss = 0
    total_lr = []
    correct = 0
    total = 0
    net.zero_grad()
    optimizer.zero_grad()
    net.train()
    loss_t_1 = 0
    for batch_idx, (inputs, targets) in enumerate(trainloader):
        inputs, targets = inputs.to(device), targets.to(device)
        with torch.set_grad_enabled(True):
            net.train()
            org_params = [deepcopy(p).data for p in deepcopy(net).parameters()]
            outputs = net(inputs)
            loss = criterion(outputs, targets)# / len(trainloader)
            try:
                loss_t = loss.item() / len(trainloader)
            except:
                loss_t = loss / len(trainloader)
            loss.backward()
            # loss_t = loss.item()
            loss_diff = (loss_t_1 - loss_t) / len(trainloader)
        
            n = len(trainloader)

            train_loss += (loss.item() / len(trainloader))
            _, predicted = outputs.max(1)
            total += targets.size(0)
            correct += predicted.eq(targets).sum().item()



            progress_bar(batch_idx, len(trainloader), 'Loss: %.3f | Acc: %.3f%% (%d/%d) | LR: %.5f'
                        % ((train_loss/(batch_idx+1))*len(trainloader), 100.*correct/total, correct, total, lr_))
            # loss_t = deepcopy(loss_t_1)

            # with torch.set_grad_enabled(True):
            optimizer.step()
            grads = [deepcopy(p.grad) for p in net.parameters()]
            optimizer.zero_grad()
            net.zero_grad()
            net.eval()
            new_params = [deepcopy(p).data for p in deepcopy(net).parameters()]
    # net.eval()
            if first:
                lr, v = LALR7(lr, n, loss_t, loss_t_1, org_params, new_params, grads, first, device=device, epoch=epoch)
                first = True
            else:
                lr = LALR7(lr, n, loss_t, loss_t_1, org_params, new_params, grads, first, v, device=device, epoch=epoch)
            # lr = LALR2(lr, grads, org_params, new_params, dt=1e-5)
            # lr = LALR3(lr, loss_diff, org_params, new_params)
            try:
                lr_ = lr.item()
            except:
                lr_ = lr
            # print(lr_)/

            for g in optimizer.param_groups:
                g['lr'] = lr_
            final_lrs.append(lr_)

            del org_params
            del new_params
            del grads

    total_loss.append(train_loss)
    return loss_t, lr_, first, final_lrs, total_loss, 100.*correct/total, v


def test(epoch):
    global best_acc
    net.eval()
    test_loss = 0
    correct = 0
    total = 0
    with torch.no_grad():
        for batch_idx, (inputs, targets) in enumerate(testloader):
            inputs, targets = inputs.to(device), targets.to(device)
            outputs = net(inputs)
            loss = criterion(outputs, targets)

            test_loss += loss.item()
            _, predicted = outputs.max(1)
            total += targets.size(0)
            correct += predicted.eq(targets).sum().item()

            progress_bar(batch_idx, len(testloader), 'Loss: %.3f | Acc: %.3f%% (%d/%d)'
                         % (test_loss/(batch_idx+1), 100.*correct/total, correct, total))

    # Save checkpoint.
    acc = 100.*correct/total
    if acc > best_acc:
        print('Saving..')
        state = {
            'net': net.state_dict(),
            'acc': acc,
            'epoch': epoch,
        }
        if not os.path.isdir('checkpoint'):
            os.mkdir('checkpoint')
        torch.save(state, './checkpoint/ckpt.pth')
        best_acc = acc
    return acc

loss_t = 0
total_loss = []
total_lr = []


lr = args.lr

final_lrs = []
total_loss = []
train_accs = []
test_accs = []

first = True
v = None
for epoch in range(start_epoch, start_epoch+200):
    loss_t, lr, first, final_lrs, total_loss, train_acc, v = train(epoch, loss_t, lr, first, final_lrs, total_loss, v)
    # total_loss.append(loss_t)
    total_lr.append(lr)
    test_acc = test(epoch)

    train_accs.append(train_acc)
    test_accs.append(test_acc)

    np.save('./lrsch_train_accs.npy', np.array(train_accs))
    np.save('./lrsch_test_accs.npy', np.array(test_accs))
    
    np.save('./lr_schedule.npy', np.array(total_loss))
    np.save('./total_lrs.npy', np.array(final_lrs))
    print("[*] Losses Saved ... Training Ended ...")
