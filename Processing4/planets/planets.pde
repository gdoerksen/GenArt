 
// Objective: generate cool planets and maybe animate them? 

// objective: a nice grey textured background? 

color background_color = #121212;

color[] planet_colors = {#BB86FC, #03DAC6, #CF6679};
color[] planet_colors_ext = {#BB86FC, #6200EE, #03DAC6, 
                            #018786, #CF6679, #B00020};

color randomColor()
{
  return planet_colors_ext[ int(random( planet_colors_ext.length - 1 )) ];
}

SolarSystemGenerator solarSystem = new SolarSystemGenerator();



void setup()
{
  size(900, 900);
  // pixelDensity(2);
}

void draw()
{
  background(background_color);

  solarSystem.sun.draw();

  for (Planet planet : solarSystem.planets)
  {
    planet.orbit();
  }

}



public class Sun 
{
  public int _x;
  public int _y;
  public int _radius;
  public color _fill_color;

  public Sun(int pos_x, int pos_y, int radius, color fill_color)
  {
    _x = pos_x;
    _y = pos_y;
    _radius = radius;
    _fill_color = fill_color;
  }
  
  public void draw()
  {
    noStroke();
    fill(_fill_color);
    ellipse(_x, _y, 2*_radius, 2*_radius);
  }
}

public class Planet
{
  public int _orbit_center_x;
  public int _orbit_center_y;
  public int _orbit_radius;
  public float _orbit_velocity_rpm;
  public color _orbit_color;
  public int _radius;
  public int _position_x;
  public int _position_y;
  public float _angle_deg;
  public color _fill_color;

  public Planet(int orbit_center_x, int orbit_center_y, int orbit_radius,
          float orbit_velocity_rpm, color orbit_color, int radius, float angle, 
          color fill_color)
  {
    _orbit_center_x = orbit_center_x;
    _orbit_center_y = orbit_center_y;
    _orbit_radius = orbit_radius;
    _orbit_velocity_rpm = orbit_velocity_rpm;
    _orbit_color = orbit_color;
    _radius = radius;
    _angle_deg = angle;
    _fill_color = fill_color;

    set_position_from_angle();
  }

  public void draw_planet()
  {
    noStroke();
    fill(_fill_color);
    ellipse(_position_x, _position_y, 2*_radius, 2*_radius);
  }

  public void draw_orbit()
  {
    stroke(#f1f1f1);
    noFill();
    ellipse(_orbit_center_x, _orbit_center_y, 2*_orbit_radius, 2*_orbit_radius);

    noStroke();
    fill(background_color);
    ellipse(_position_x, _position_y, 2*_radius+20, 2*_radius+20);

  }

  public void orbit()
  {
    float angular_change_deg = _orbit_velocity_rpm * 60 / 360;
    set_angle(_angle_deg+angular_change_deg);
    draw_orbit();
    draw_planet();
  }

  private void set_angle(float angle_deg)
  {
    _angle_deg = angle_deg % 360;
    set_position_from_angle();
  }

  private void set_position_from_angle()
  {
    _position_x = _orbit_center_x + int(_orbit_radius*cos(_angle_deg / 180 * PI));
    _position_y = _orbit_center_y + int(_orbit_radius*sin(_angle_deg / 180 * PI));
  }

}

int PLANET_MAX_RADIUS = 25;
int PLANET_MIN_RADIUS = 5;


public class SolarSystemGenerator
{
  ArrayList<Planet> planets = new ArrayList<Planet>();
  public Sun sun;

  public SolarSystemGenerator()
  {
    sun = new Sun(450, 450, int(random(50, 100)), randomColor());

    int orbit_radius = sun._radius;

    while (orbit_radius < 450)
    {
      int offset = int( random(25, 100) );
      orbit_radius += offset;
      if (orbit_radius > 450)
      {
        break;
      }
      // int new_planet_radius = int( random(PLANET_MIN_RADIUS, min(PLANET_MAX_RADIUS, offset ) ) ); 
      int new_planet_radius = int( random(5, 25) ); 
      orbit_radius += new_planet_radius;
      if (orbit_radius > 450)
      {
        break;
      }
 
      float orbit_velocity_rpm = random(0.25, 1);
      int angle = int(random(0,359));

      planets.add(new Planet(sun._x, sun._y, orbit_radius, orbit_velocity_rpm, #aaaaaa, new_planet_radius, angle, randomColor()));

    }

  }

}