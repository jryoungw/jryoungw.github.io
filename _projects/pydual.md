---
title: "PyDual"
description: "Dual number automatic differentiation library with CPU/GPU support. Implements forward-mode AD via dual numbers, with PyTorch-compatible API and custom CUDA kernels for high-performance gradient computation."
status: active
tags: [Python, C++, CUDA, Automatic Differentiation]
github: "https://github.com/YOUR_USERNAME/pydual"
demo: ""
paper: ""
---

## Overview

PyDual is a from-scratch implementation of forward-mode automatic differentiation using dual numbers, supporting both CPU and GPU execution.

## Key Features

- **Dual number arithmetic**: Full operator overloading for `+`, `-`, `*`, `/`, `**`
- **CUDA kernels**: Custom GPU kernels for element-wise dual operations
- **PyTorch integration**: Drop-in compatibility with `torch.Tensor`
- **Neural network support**: ResNet training on CIFAR-10 validated

## Mathematical Foundation

A dual number $a + b\varepsilon$ where $\varepsilon^2 = 0$ encodes both a value and its derivative simultaneously. For any smooth function $f$:

$$f(a + b\varepsilon) = f(a) + b f'(a)\varepsilon$$

This gives exact first-order derivatives in a single forward pass.
