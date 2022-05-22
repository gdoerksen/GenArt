
float z = 0.0;

void setup()
{
  size(900,900);
}

void draw()
{
  perlin2D(z);
  z += 0.01; 
}

void perlin2D(float z)
{
  float freq = map(mouseY, 0, height, 0, 1);
  // float z = map(mouseX, 0, width, 0, 1);
  
  loadPixels();
  for (int y = 0; y < height; y++)
  {
    for ( int x = 0; x < width; x++)
    {
      int i = x + y * width;
      float n = noise(x * freq, y * freq, z);
      pixels[i] = color(map(n, 0, 1, 0, 255));
    }
  }
  updatePixels();
}

