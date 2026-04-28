# Terrain Classification and Adaptive Speed Control

## Overview

This project is a machine learning–based terrain recognition system designed for autonomous rover navigation. The system analyzes terrain images or live camera frames, classifies the surface type, evaluates terrain safety, and recommends an adaptive rover speed based on risk level.

The output is displayed in real time through the terminal or console.

## Objective

Build an intelligent software system that can:

- Accept terrain images or camera frames as input
- Classify terrain using a trained machine learning model
- Display terrain type with confidence score
- Determine terrain safety level
- Recommend rover speed based on terrain condition
- Run inference in real time through terminal/console

## Terrain Classes

The model classifies terrain into the following categories:

1. Smooth Ground  
2. Gravel  
3. Sand  
4. Rock Field  

## Speed Decision Logic

| Terrain Type   | Risk Level | Recommended Rover Speed |
|----------------|------------|--------------------------|
| Smooth Ground  | Safe       | 70–100 km/h             |
| Gravel         | Moderate   | 40–60 km/h              |
| Sand           | High       | 20–40 km/h              |
| Rock Field     | Very High  | 5–20 km/h               |

## Example Output

```text
Terrain Detected: Sand
Confidence: 87%
Risk Level: High
Recommended Rover Speed: 25 km/h
