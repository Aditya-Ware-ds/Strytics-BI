const express = require('express');
const bodyParser = require('body-parser');
const path = require('path');
const multer = require('multer');
const { parse } = require('csv-parse');
const { spawn } = require('child_process');

const app = express();
const port = process.env.PORT || 3000;

app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, './'));

// Configure Multer for file uploads
const storage = multer.memoryStorage();
const upload = multer({ storage: storage });

// Basic route for the root path
app.get('/', (req, res) => {
    res.render('frontend.ejs');
});

app.post('/', upload.single('csvFile'), (req, res) => {
    const userInput = req.body.message;
    console.log(userInput);

    if (!req.file) {
        return res.status(400).send('No file was uploaded.');
    }

    const csvBuffer = req.file.buffer;
    const csvContent = csvBuffer.toString('utf-8');

    // Parse CSV content
    parse(csvContent, { columns: true }, (err, records) => {
        if (err) {
            return res.status(500).send('Error parsing CSV file.');
        }

        console.log(records);

        // Spawn a child process to run the Python script
        const pythonProcess = spawn('python', ['eli.py']);

        // Send data to the Python script
        const dataToSend = { userInput, records };
        pythonProcess.stdin.write(JSON.stringify(dataToSend));
        pythonProcess.stdin.end();

        // Your further processing with the parsed CSV data

        

        res.send('File uploaded and processed successfully.');
    });
});

// Start the server
app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});
