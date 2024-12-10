# Pathology Image Analysis Pipeline

This repository contains a pipeline for analyzing pathology images using various AI models (GPT-4, Claude-3, Claude-3.5) and evaluating their performance with different types of image labels/watermarks.

## Pipeline Overview

The pipeline consists of four main steps:

1. Image Processing (`image-processing-notebook_watermark.ipynb`)
2. Model Inference (`inference_llms_watermark.ipynb`, `inference_llms_promptengineering.ipynb`)
3. Score Combination (`combine_score_results.ipynb`, `combine_score_results_watermark.ipynb`)
4. Visualization and Analysis (`PathoPrompt Results.Rmd`)

## Prerequisites

### Python Environment
- Python 3.11+
- Required packages:
  ```
  pandas
  pillow
  cairosvg
  numpy
  tqdm
  anthropic
  openai
  python-dotenv
  ```

### R Environment
- R 4.0+
- Required packages:
  ```
  ggplot2
  readxl
  dplyr
  tidyr
  gridExtra
  FSA
  rstatix
  scales
  RColorBrewer
  openxlsx
  svglite
  networkD3
  htmlwidgets
  webshot2
  rsvg
  ```

## Step-by-Step Usage

### 1. Image Processing
Run `image-processing-notebook_watermark.ipynb` to:
- Process original pathology images
- Add labels/watermarks based on metadata
- Generate modified images for analysis

Key parameters:
- `label_width_pct`: Width of label as percentage of image
- `label_height_pct`: Height of label as percentage of image
- `alpha`: Transparency of label (0-100)

### 2. Model Inference
Run the inference notebooks in this order:

a. `inference_llms_watermark.ipynb`:
- Processes images with standard prompts
- Supports multiple AI models (GPT-4, Claude-3, Claude-3.5)
- Handles both labeled and unlabeled images

b. `inference_llms_promptengineering.ipynb`:
- Similar to watermark inference but with engineered prompts
- Tests model behavior with different prompt strategies

Required environment variables:
- `API_KEY_CLAUDE`: Anthropic API key
- `OPENAI_API_KEY`: OpenAI API key

### 3. Score Combination
Run `combine_score_results_watermark.ipynb` to:
- Combine results from different models
- Calculate accuracy scores
- Process diagnostic outputs
- Generate combined analysis files

### 4. Visualization and Analysis
Run `PathoPrompt Results.Rmd` to:
- Generate visualization plots
- Perform statistical analysis
- Create summary tables
- Export results to Excel

## Directory Structure

```
project/
│
├── notebooks/
│   ├── image-processing-notebook_watermark.ipynb
│   ├── inference_llms_watermark.ipynb
│   ├── inference_llms_promptengineering.ipynb
│   └── combine_score_results_watermark.ipynb
│
├── analysis/
│   └── PathoPrompt Results.Rmd
│
├── data/
│   ├── input/
│   │   └── Patient_Metadata_long.xlsx
│   └── output/
│       └── combined_analysis_results.xlsx
│
└── figures/
    └── [generated plots and visualizations]
```

## Output Files

- `combined_analysis_results.xlsx`: Contains combined model predictions and accuracy metrics
- `combined_analysis_results_watermark.xlsx`: Results specific to watermark experiments
- Generated figures in SVG format in the figures directory

## Notes

- Images must be under 4MB for API processing
- Batch processing is used to handle rate limits
- Set `limit_items=True` for testing with smaller datasets
- Chrome and Adobe Reader should be closed when generating Sankey diagrams

## Troubleshooting

- If API calls fail, check rate limits and API keys
- For image processing errors, verify file paths and image sizes
- For R visualization issues, ensure all required packages are installed

