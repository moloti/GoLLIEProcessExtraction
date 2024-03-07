#!/bin/sh
#BSUB -q gpua100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -J jobgolliedaniel13
#BSUB -n 4
#BSUB -W 06:00
#BSUB -R "rusage[mem=12GB]"
#BSUB -u s213709@dtu.dk
## -- send notification at start --
#BSUB -B
## -- send notification at completion--
#BSUB -N
#BSUB -o logs/%J.out
#BSUB -e logs/%J.err

## <loading of modules, dependencies etc.>

echo "Start training..."

source genv10/bin/activate

echo CUDA_VISIBLE_DEVICES "${CUDA_VISIBLE_DEVICES}"

CONFIGS_FOLDER="configs/model_configs/eval"

python -m src.run ${CONFIGS_FOLDER}/GoLLIE-13B_CodeLLaMA_medical.yaml