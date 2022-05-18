PImage img;
Main main;

void setup()
{
 size(900, 900, P3D);
    //img = loadImage("michele-caliani_square.jpg");
    img = loadImage("chess-beytlik_square.jpg");
    //img = loadImage("brett-sayles_square.jpg");
    img.resize(900,900);
    
   background(#f1f1f1);
   float tiles = 90;
   //float tiles = mouseX;
   float tileSize = width/tiles;
    main = new Main(tiles, tileSize);
}

void draw()
{
  main.looop();

}

public class Main
{
  public float _tiles;
  public float _tileSize;
  
  public float _b_mag = 0;
  public boolean _increase = true; 
  
  public Main(float tiles, float tileSize)
  {
    _tiles = tiles;
    _tileSize = tileSize;
  }
  
  public void setBackground(float colorr)
  {
    background(colorr);
  }
  
  public void setTiles(float tiles)
  {
   _tiles = tiles;
  }
  
  public void setTileSize(float tileSize)
  {
   _tileSize = tileSize; 
  }
  
  public void looop()
  {
    background(#f1f1f1);
    //_tiles = 90;
    //_tileSize = width/_tiles;
    sphereDetail(3);
    fill(0);
    noStroke();
    
    //_b_mag_stepper();
    
    push();
    
    translate(width/2, height/2);
    rotateY(radians(frameCount));
    for (int x=0; x<_tiles; x++)
    {
      for (int y=0; y<_tiles; y++)
      {
        rotateAroundCenter(x,y);
      }
    }
     
    pop();
  }
  
  private void _b_mag_stepper()
  {
    if (_b_mag >= 1)
    {
      _b_mag = 1.0;
      _increase = false;
    }
    else if (_b_mag <= 0)
    {
      _b_mag = 0.0;
      _increase = true;
    }
     
    if (_increase)
    {
      _b_mag += 0.001;
    }
    else
    {
      _b_mag -= 0.001;
    }   
  }
  
  private void rotateAroundCenter(int x, int y)
  {
    color c = img.get( int(x*_tileSize), int(y*_tileSize));
        
    float b = map(brightness(c),0,255, 1-_b_mag, 0+_b_mag);
   
    float z = map(b, 0,1, -100, 100);
        
    push();
    translate(x*_tileSize - width/2, y*_tileSize - height/2, z);
    
    sphere(_tileSize*b*0.5);
    pop();
  }
  
}
