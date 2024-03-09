#!/bin/sh
#BSUB -q gpua100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -J jobgolliedaniel
#BSUB -n 4
#BSUB -W 03:00
#BSUB -R "rusage[mem=12GB] select[gpu80gb]"
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

python -m src.run ${CONFIGS_FOLDER}/GoLLIE-34B_CodeLLaMA_medical.yaml