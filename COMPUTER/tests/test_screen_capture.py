from ..perception.screen_capture import get_monitors, capture_screen
from ..perception.image_analyzer import analyze_image

if __name__ == "__main__":
    frame = capture_screen() # takes a screenshot 
    size, data_type, color, brightness, lighting, blue_channel, green_channel, red_channel, dominant_intensity, dominant_color = analyze_image(frame)

    print(f"""Size: {size}, 
        Data Type: {data_type}, 
        Color: {color}, 
        Brightness: {brightness}, 
        Lighting: {lighting}, 
        Blue Channel: {blue_channel}, 
        Green Channel: {green_channel},
        Red Channel: {red_channel}, 
        Dominant Intensity: {dominant_intensity},
        Dominant Color: {dominant_color}""")
    
def test_get_monitors():
    monitors = get_monitors()
    assert isinstance(monitors, list)
    assert len(monitors) > 0 