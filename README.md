# Movie Recommendation System

A simple movie recommendation system built using **FastAPI** and **Python** libraries, The application uses a preloaded dataset of movies to recommend similar titles based on user input.
the app is not fully working yet, im looking for contributors.

Goal is to make a nice UI to get user preferences, and finish the recommendation algorithm .

---

## Technologies Used

### Backend
- **[FastAPI](https://fastapi.tiangolo.com/)**: For building API endpoints.
- **[Uvicorn](https://www.uvicorn.org/)**: ASGI server to run the FastAPI app.
- **[Pandas](https://pandas.pydata.org/)**: For data manipulation.
- **[Scikit-learn](https://scikit-learn.org/)**: To calculate similarity scores.

### Frontend
- **HTML/CSS/JavaScript**: Simple static files for the user interface.

---

## Getting Started

### Prerequisites
- Python 3.8 or above
- pip (Python package manager)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/BenMekkiMouad/movies-recommendation-system.git
   cd movies-recommendation-system
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the FastAPI server:
   ```bash
   uvicorn app.main:app --reload
   ```

4. Open your browser and navigate to:
   ```
   http://127.0.0.1:8000
   ```

---

## Project Structure

```
movies-recommendation-system/
├── app/
│   ├── data/
│   │   ├── movies.csv   # dataset of movies
│   ├── static/
│   │   ├── style.css         # Stylesheet for the web interface
│   │   └── script.js         # JavaScript for dynamic frontend functionality
│   ├── templates/
│   │   └── index.html        # Main HTML file
│   ├── main.py               # FastAPI application
│   ├── recommendation_engine.py # Movie recommendation logic               
├── requirements.txt          # Python dependencies
├── IDEA.ipynb                 # Get to know the project in depth
├── README.md                 # Documentation (this file)
```


---

## Contribution

Contributions are welcome! Follow these steps to contribute:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Make your changes and commit them:
   ```bash
   git commit -m "Add new feature"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request on GitHub.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Acknowledgments

- Built using [FastAPI](https://fastapi.tiangolo.com/).
- Inspired by the need for simple recommendation systems.

---

## Contact

For any questions or feedback, feel free to reach out:
- **Author**: Mouad Ben Mekki
- **GitHub**: [BenMekkiMouad](https://github.com/BenMekkiMouad)

