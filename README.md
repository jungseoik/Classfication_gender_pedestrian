# Classfication_gender_pedestrian

conda create -n gender python==3.10 -y
conda activate gender

pip install -r requirements.txt
pip uninstall ultralytics
git clone https://github.com/jyrainer/ultralytics.git
cd ultralytics
git checkout new_exp_yolov11-8.3.66
pip install -e .