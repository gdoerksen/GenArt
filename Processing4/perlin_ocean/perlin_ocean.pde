
float z = 0.0;
color[] greenBlueOcean = {#064E40, #0DAD8D, #8DD8CC, #30BFBF, #0C98BA, #1164B4};
float[] bnd = {0.0, 0.2, 0.4, 0.6, 0.8, 1.0};

Gradient grad = new Gradient( greenBlueOcean, bnd );

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
  float freq = 0.02;

  loadPixels();
  for (int y = 0; y < height; y++)
  {
    for ( int x = 0; x < width; x++)
    {
      int i = x + y * width;
      float n = noise(x * freq, y * freq, z);
      // pixels[i] = color(map(n, 0, 1, 0, 255));
      pixels[i] = grad.getColor(n);
    }
  }
  updatePixels();
}

public class Gradient
{
  private color[] _colors;
  private float[] _bounds;

  public Gradient( color[] colors, float[] bounds)
  {
    _colors = colors;
    _bounds = bounds;
  }

  public color getColor(float amt)
  {
    for (int i = 1; i < _bounds.length; i++)
    {
      if (amt < _bounds[i])
      {
        float percent = (amt - _bounds[i-1]) / (_bounds[i] - _bounds[i-1]);
        return lerpColor(_colors[i-1], _colors[i], percent);
      }
    }

    return _colors[_colors.length - 1];
  }
}
