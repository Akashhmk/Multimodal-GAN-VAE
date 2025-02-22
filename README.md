# Multimodal Generative Modeling Using GANs and VAEs
📌 Project Overview

This project integrates Variational Autoencoders (VAE) and Generative Adversarial Networks (GAN) to generate high-quality MNIST-like images while learning a meaningful latent space.

🔥 Key Features

✅ VAE Encoder: Uses convolutional layers and the Reparameterization Trick to extract latent features.
✅ VAE Decoder (Generator): Reconstructs images from latent vectors using transposed convolutions.
✅ GAN Discriminator: A CNN-based classifier that helps improve image sharpness.
✅ Hybrid Training: Combines VAE’s reconstruction loss with GAN’s adversarial loss to generate better-quality digits.

🏗️ Project Architecture
	•	Variational Autoencoder (VAE):
	•	Learns a compressed latent representation of images.
	•	Uses KL divergence loss to ensure meaningful latent space learning.
	•	Generative Adversarial Network (GAN):
	•	Enhances generated images by forcing the decoder to create sharp, realistic images.
	•	The discriminator learns to distinguish real vs. generated images.

🛠️ Technologies Used
	•	Python
	•	TensorFlow & Keras
	•	MNIST Dataset
	•	NumPy & Matplotlib
