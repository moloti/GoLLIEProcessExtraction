#!/bin/sh
#BSUB -q gpua100
#BSUB -gpu "num=2:mode=exclusive_process"
#BSUB -J jobnerdaniel
#BSUB -n 8
#BSUB -W 01:30
#BSUB -R "rusage[mem=100GB]"
#BSUB -R "select[sxm2]"
#BSUB -u s213709@dtu.dk
## -- send notification at start --
#BSUB -B
## -- send notification at completion--
#BSUB -N
#BSUB -o logs/%J.out
#BSUB -e logs/%J.err

## <loading of modules, dependencies etc.>

source genv10/bin/activate

echo CUDA_VISIBLE_DEVICES "${CUDA_VISIBLE_DEVICES}"

CONFIGS_FOLDER="configs/model_configs/eval"

python3 -m src.run ${CONFIGS_FOLDER}/GoLLIE-34B_CodeLLaMA_medical.yaml