from ComicTextDetector.inference import model2annotations

img_dir = r'ComicTextDetector/data/examples'
model_path = r'ComicTextDetector/data/comictextdetector.pt'
img_dir = r'ComicTextDetector/data/examples'                              # can be dir list
save_dir = r'ComicTextDetector/data/examples/annotations'
model2annotations(model_path, img_dir, save_dir, save_json=False)
