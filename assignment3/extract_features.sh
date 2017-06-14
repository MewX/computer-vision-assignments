# csh
# $1: image directory (without slash), containing tasks.txt (all image names)
# out: an *.mat file

# preq:
# feature model definition: python_features/deploy_features.prototxt
# feature model caffe net: checkpoints/VGG_ILSVRC_16_layers.caffemodel

python py_caffe_feat_extract.py --model_def_path python_features/deploy_features.prototxt --model_path checkpoints/VGG_ILSVRC_16_layers.caffemodel -i "$1/" --filter "$1/tasks.txt" -o "$1/"
