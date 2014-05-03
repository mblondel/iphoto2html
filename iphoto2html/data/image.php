<?php

// File and new size
$filename = $_GET['filename'];
$newheight = $_GET['height'];

if(!isset($newheight))
    $newheight = 750;

// Content type
header('Content-Type: image/jpeg');

// Get new sizes
list($width, $height) = getimagesize($filename);
$percent = $newheight / $height;
$newwidth = $width * $percent;

// Load
$thumb = imagecreatetruecolor($newwidth, $newheight);
$source = imagecreatefromjpeg($filename);

// Resize
imagecopyresampled($thumb, $source, 0, 0, 0, 0, $newwidth, $newheight, $width, $height);

// Output and free memory
imagejpeg($thumb, null, 95);
imagedestroy($thumb);
?>

