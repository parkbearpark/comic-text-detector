from inference import model2annotations

img_dir = r'data/examples'
model_path = r'data/comictextdetector.pt'
img_dir = r'data/examples'                              # can be dir list
save_dir = r'data/examples/annotations'
model2annotations(model_path, img_dir, save_dir, save_json=False)