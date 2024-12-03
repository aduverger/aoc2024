use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() -> io::Result<()> {
    let path = "./input.txt";
    let file = File::open(path)?;
    let reader = io::BufReader::new(file);

    let mut left_list = Vec::new();
    let mut right_list = Vec::new();

    // Parse the input file
    for line in reader.lines() {
        let line = line?;
        let parts: Vec<&str> = line.split_whitespace().collect();
        if parts.len() == 2 {
            let left = parts[0].parse::<i32>().unwrap();
            let right = parts[1].parse::<i32>().unwrap();
            left_list.push(left);
            right_list.push(right);
        }
    }

    // Sort the lists
    left_list.sort_unstable();
    right_list.sort_unstable();

    // Calculate distances
    let mut distances = 0;
    for (&left, &right) in left_list.iter().zip(right_list.iter()) {
        distances += (left - right).abs();
    }

    println!("{}", distances);

    // Calculate total count
    let mut total_count = 0;
    for &left in &left_list {
        let left_count = right_list.iter().filter(|&&right| right == left).count() as i32;
        total_count += left * left_count;
    }

    println!("{}", total_count);

    Ok(())
}
