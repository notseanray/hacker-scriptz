use image::imageops::grayscale;
use image::{image_dimensions, open};
use std::time::Instant;
use std::{env, fs};

fn main() -> std::io::Result<()> {
    let startup = Instant::now();
    let args: Vec<String> = env::args().skip(1).collect();

    let layers = match args.len() {
        2.. => args[1].parse().unwrap(),
        _ => 1,
    };

    let image = open(args[0].clone()).unwrap();

    let _ = fs::remove_file("./grayscale.jpeg");

    let _ = fs::remove_dir_all("./layers");

    grayscale(&image).save("./grayscale.jpeg").unwrap();

    if args.len() < 2 {
        println!("complete in {:#?}", startup.elapsed());
        return Ok(());
    }

    let _ = fs::create_dir("./layers");

    let group = 255 / layers;

    //let image = open(args[0].clone()).unwrap().into_bytes();
    let image = open("./grayscale.jpeg").unwrap().into_bytes();

    let (w, h) = image_dimensions(args[0].clone()).unwrap();

    println!("{w}x{h} pixel buffer: {} in {:#?}", image.len(), startup.elapsed());

    let mut start = 0;
    let mut end = group;

    for i in 0..layers {
        let frametime = Instant::now();
        let mut pixels: Vec<u8> = vec![0; image.len()];
        for (e, x) in image.iter().enumerate() {
            if x < &start || x > &end {
                continue;
            }
            pixels[e] = *x;
        }
        let i = i + 1;
        let path = format!("./layers/{}.jpeg", i);
        if args.len() > 2 && args[2] == "edge".to_string() {
            let detect = edge_detection::canny(
                image::ImageBuffer::from_raw(w, h, pixels).unwrap(),
                0.8,
                0.2,
                0.001,
            );
            let detect = image::imageops::contrast(&detect.as_image(), f32::MAX);
            image::imageops::grayscale(&detect).save(path).unwrap();
        } else {
            let layer = image::DynamicImage::ImageLuma8(
                image::ImageBuffer::from_raw(w, h, pixels).unwrap(),
            );
            layer.save(path).unwrap();
        }
        println!("completed layer: {} in {:#?}", i, frametime.elapsed());
        if 255 - group < end {
            break;
        }
        start += group;
        end += group;
    }

    println!("complete in {:#?}", startup.elapsed());

    Ok(())
}
