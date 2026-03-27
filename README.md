# Football Player Tracking and Match Analytics

A computer vision project for tracking football players, ball movement, team assignment, camera motion, and speed/distance estimation from match footage using YOLO and Python.

## Overview

This project analyzes football match videos and generates structured visual insights such as:
- Player detection and tracking
- Ball tracking
- Team assignment based on visual cues
- Camera movement estimation
- View transformation
- Speed and distance estimation

The system is designed as a modular pipeline, making it easy to extend for advanced sports analytics use cases.

## Features

- YOLO-based object detection
- Multi-object tracking for players and ball
- Team classification / assignment
- Camera motion estimation
- Perspective / view transformation
- Speed and distance estimation
- Annotated video generation

## Demo Preview

![Football Player Tracking and Match Analytics](assets/output_preview.gif)

## Project Structure

`text
football-player-tracking/
├── src/
├── notebooks/
├── models/
├── data/
├── outputs/
├── assets/
├── requirements.txt
└── README.md