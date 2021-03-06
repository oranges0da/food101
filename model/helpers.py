import torch
import matplotlib.pyplot as plt
from data_loader.helpers import imshow
from torchsummary import summary

# visualize and summarize model archetecture with torchsummary
def model_summary(model):
    return summary(model, input_size=(3, 224, 224))

# visualize model predictions with matplotlib
def visualize_model(model, num_images=6, trainloader=None):
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    was_training = model.training
    model.eval()
    images_so_far = 0
    fig = plt.figure()

    with torch.no_grad():
        for i, (inputs, labels) in enumerate(trainloader):
            inputs = inputs.to(device)
            labels = labels.to(device)

            outputs = model(inputs)
            _, preds = torch.max(outputs, 1)

            for j in range(inputs.size()[0]):
                images_so_far += 1
                ax = plt.subplot(num_images//2, 2, images_so_far)
                ax.axis('off')
                imshow(inputs.cpu().data[j])

                if images_so_far == num_images:
                    model.train(mode=was_training)
                    return
        model.train(mode=was_training)