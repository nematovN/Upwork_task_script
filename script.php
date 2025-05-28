<?php

function readLines($filename) {
    return file_exists($filename) ? array_map('trim', file($filename)) : [];
}

function removeContinuousCharacters($str) {
    return preg_replace('/(.)\1+/', '$1', $str);
}

function removeStopwords($str, $stopwords) {
    foreach ($stopwords as $word) {
        $str = preg_replace('/\b' . preg_quote($word, '/') . '\b/i', '', $str);
    }
    return trim(preg_replace('/\s+/', ' ', $str));
}

function generateSimilarWords($str, $similarMap) {
    $results = [];
    foreach ($similarMap as $base => $similars) {
        if (stripos($str, $base) !== false) {
            foreach ($similars as $variant) {
                $results[] = str_ireplace($base, $variant, $str);
            }
        }
    }
    return $results;
}

function removeVowels($str) {
    return preg_replace('/[aeiouAEIOU]/', '', $str);
}

function convertNumbers($str) {
    $numWords = ['0'=>'Zero','1'=>'One','2'=>'Two','3'=>'Three','4'=>'Four','5'=>'Five','6'=>'Six','7'=>'Seven','8'=>'Eight','9'=>'Nine'];
    $wordNums = array_flip($numWords);

    // Numbers to Words
    $str = preg_replace_callback('/\d/', function($m) use ($numWords) {
        return $numWords[$m[0]];
    }, $str);

    // Words to Numbers
    $str = preg_replace_callback('/\b(' . implode('|', array_keys($wordNums)) . ')\b/i', function($m) use ($wordNums) {
        return $wordNums[ucfirst(strtolower($m[0]))];
    }, $str);

    return $str;
}

function removeConsecutiveVowelsOrConsonants($str) {
    return preg_replace('/([aeiou]{2,}|[^aeiou\s]{2,})/i', '', $str);
}

// 🔹 Fayllarni o'qish
$names = readLines("names.txt");
$stopwords = readLines("stopwords.txt");
$similarLines = readLines("similar.txt");

$similarMap = [];
foreach ($similarLines as $line) {
    $parts = explode('=', $line);
    if (count($parts) === 2) {
        $key = trim($parts[0]);
        $similarMap[$key] = array_map('trim', explode(',', $parts[1]));
    }
}

// 🔹 CSV fayl ochish
$output = fopen("output.csv", "w");
fputcsv($output, ['originalstring', 'Listofgenerated']);

foreach ($names as $name) {
    $generated = [];

    // Similar
    $generated = array_merge($generated, generateSimilarWords($name, $similarMap));

    // Remove continuous characters
    $generated[] = removeContinuousCharacters($name);

    // Remove consecutive vowels/consonants
    $generated[] = removeConsecutiveVowelsOrConsonants($name);

    // Remove stopwords
    $generated[] = removeStopwords($name, $stopwords);

    // Remove vowels
    $generated[] = removeVowels($name);

    // Convert numbers and words
    $generated[] = convertNumbers($name);

    $generated = array_unique(array_filter($generated));
    fputcsv($output, [$name, implode(",", $generated)]);
}

fclose($output);

echo "✅ output.csv generated done.\n";

?>
