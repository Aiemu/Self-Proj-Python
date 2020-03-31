from imagenet1000 import labels
import skimage, numpy, torch, torchvision, ssl
import matplotlib.pyplot as plt

ssl._create_default_https_context = ssl._create_unverified_context

def segmentation(imagedir):
    image = skimage.io.imread(imagedir,plugin='matplotlib')
    image = skimage.transform.resize(image, (520, 520), anti_aliasing=True)
    image = numpy.transpose(image, (2, 0, 1))
    image = image.astype(numpy.float32)

    input = torch.from_numpy(image)
    normalize = torchvision.transforms.Normalize(mean=[0.485, 0.456, 0.406],std=[0.229, 0.224, 0.225])
    input = normalize(input)
    input = torch.unsqueeze(input, 0)
    
    fcn_resnet101 = torchvision.models.segmentation.fcn_resnet101(pretrained=True)
    fcn_resnet101.eval()

    output = fcn_resnet101(input)
    output = output['out']
    output = output.squeeze().argmax()

    path = 'output/'+imagedir
    plt.imsave(path, output)
    return path