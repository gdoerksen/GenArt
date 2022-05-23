 
// Objective: generate cool planets and maybe animate them? 

// objective: a nice grey textured background? 

// int sun_x = int(width / 2);
// int sun_y = height;
int sun_x = 450;
int sun_y = 450;
float sun_diameter = 200; 

Planet p1 = new Planet(sun_x, sun_y, 300, 1, #f1f1f1, 50, 0, #aaaaaa);

void setup()
{
  size(900, 900);

}

void draw()
{
  background(#151515);

  noStroke();
  fill(#aaaaaa);
  ellipse(sun_x, sun_y, sun_diameter, sun_diameter);

  // p1.draw();
  p1.orbit();

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

  public void draw()
  {
    noStroke();
    fill(_fill_color);
    ellipse(_position_x, _position_y, 2*_radius, 2*_radius);
  }

  public void orbit()
  {
    float angular_change_deg = _orbit_velocity_rpm * 60 / 360;
    set_angle(_angle_deg+angular_change_deg);
    draw();
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
