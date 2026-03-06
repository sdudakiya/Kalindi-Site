const sharp = require('sharp');
const fs = require('fs');

async function convertImage() {
  try {
    const inputBuffer = fs.readFileSync('/Users/chakshu/Desktop/Kalindi-Site/Kalindi Marketing Logo.png');
    await sharp(inputBuffer)
      .webp({ quality: 80 })
      .toFile('/Users/chakshu/Desktop/Kalindi-Site/assets/logo.webp');
    console.log('Successfully converted Kalindi Marketing Logo.png to assets/logo.webp');
  } catch (error) {
    console.error('Error converting image:', error);
  }
}

convertImage();
