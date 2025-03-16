from transformers import pipeline, AutoImageProcessor, AutoModelForImageClassification
from PIL import Image
import torch  


def classify_wound_using_pipeline(image_path):
    pipe = pipeline("image-classification", model="Hemg/Wound-classification")
    image = Image.open(image_path).convert("RGB")
    predictions = pipe(image)
    print("Predictions using pipeline:")
    for pred in predictions:
        print(f"{pred['label']}: {pred['score']:.4f}")


def classify_wound_directly(image_path):
    processor = AutoImageProcessor.from_pretrained("Hemg/Wound-classification")
    model = AutoModelForImageClassification.from_pretrained("Hemg/Wound-classification")
    image = Image.open(image_path).convert("RGB")
    inputs = processor(images=image, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
    predicted_class_idx = logits.argmax().item()
    predicted_class_label = model.config.id2label[predicted_class_idx]
    predicted_class_score = torch.softmax(logits, dim=1)[0, predicted_class_idx].item()
    print("\nPrediction using direct model loading:")
    print(f"Predicted Class: {predicted_class_label}")
    print(f"Confidence Score: {predicted_class_score:.4f}")
    
    





def main():
    image_path = "venous2.jpg"  
    classify_wound_using_pipeline(image_path)
    classify_wound_directly(image_path)
    


if __name__ == "__main__":
    main()