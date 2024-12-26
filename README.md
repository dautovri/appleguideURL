# Apple Guides URL Decoder 📜

This project provides tools to decode URLs from Apple Guides, extract location descriptions, and collect Apple IDs from the decoded data.

## URL Formats 🌐

Apple Guides URLs can exist in several forms:

- Curated by Apple or other publishers: 
  ```
  https://guides.apple.com/?pp=16477572344376014386&lsp=9902&name=hyperlocal
  ```
- User-created guides: 
  ```
  https://guides.apple.com/?ug=GUIDENAME-APPLEPLACEIDS-APPLEIPLACEID%3D
  ```

### Example URL

```
https://guides.apple.com/?ug=CgtDb2ZmZWUgVHJpcBINCK5NELnhr%2FnwqvPSKxINCK5NEIDNk8WaqcWwPhINCK5NEODH9sObxvSqOxINCK5NEJGZhqvmhqfCIhINCK5NEPzqnpiH1vfBeRIOCK5NEMzYusHXgunY7gESDgiuTRDQy9flycmh7P4BEg4Irk0Q9aqhv5aaxYeQARINCK5NEP70qsqh4a3cXBINCK5NEPH9lMD31NGsahIOCK5NEIHK5vD1tdX7rAESDQiuTRCo1p31%2FNiZ0C4SDQiuTRC%2B%2FZXS0rbkqngSDgiuTRC5%2F5XLk7SfzoUBEg4Irk0QxM7mhe6Yx6X%2BARINCK5NEMej3cf6j4v7WhINCK5NEMSkxOrBx67eOQ%3D%3D
```

## Features ✨

- Decode URL parameters
- Extract location descriptions
- Collect Apple IDs from protobuf fields

## Installation 🛠️

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/appleguides.git
    ```
2. Navigate to the project directory:
    ```sh
    cd appleguides
    ```
3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage 🚀

1. Place your URLs in the `urls.txt` file, one URL per line.
2. Run the script to decode the URLs and extract information:
    ```sh
    python appleGuide2appleIDs.py
    ```

## Example Output 📊

```

Processing URL: https://guides.apple.com/?ug=...
Decoded URL parameter: ...
Decoded bytes: b'...'

Guide Name: Coffee Trip
 Apple Maps ID 1 : I...
 Apple Maps ID 2 : I...
 ...

Processing URL: https://guides.apple.com/?ug=...
Decoded URL parameter: ...
Decoded bytes: b'...'

Guide Name: Nice to visit
 Apple Maps ID 1 : I...
 Apple Maps ID 2 : I...
 ...
```

## Contributing 🤝

Contributions are welcome! Please open an issue or submit a pull request.

## Domains 🌍

- guide1-n.apple.com
- guide2-n.apple.com
- guide.apple.com
- guidejp1-n.apple.com
- guidejp2.apple.com
- guidejp2-n.apple.com
- guidejp-n.apple.com