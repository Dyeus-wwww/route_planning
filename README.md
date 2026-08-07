# 🚇 Hong Kong Subway Route Planner

A Python-based route planning tool for the Hong Kong MTR (Mass Transit Railway) system. Given any two locations in Hong Kong, this project finds the nearest subway stations and computes the shortest path between them using Dijkstra's algorithm with real-world distances.

---

## 📋 Features

- **Location-to-Station Matching** — Automatically finds the nearest MTR station to any given address or landmark in Hong Kong
- **Shortest Path Calculation** — Uses Dijkstra's algorithm to find the optimal route between stations
- **Real-World Distances** — Fetches actual walking distances between adjacent stations via the AMap (高德地图) API
- **Complete Route Output** — Returns the full journey from origin to destination, including the walking segments to/from stations

---

## 🗂️ Project Structure

| File | Description |
|------|-------------|
| `main_search.py` | Main entry point — handles user input and orchestrates the full search flow |
| `route_api.py` | Core routing engine — builds the station graph and runs Dijkstra's algorithm |
| `route_find.py` | Geocoding utility — fetches coordinates via AMap API and manages station data |
| `subway.csv` | Hong Kong MTR station dataset (name, line, longitude, latitude) |

---

## ⚙️ How It Works

1. **Input** — User provides a start and end location (in **Simplified Chinese**)
2. **Geocoding** — `route_find.py` queries the AMap API to get GPS coordinates for both locations
3. **Nearest Station** — `main_search.py` calculates the closest MTR station to each coordinate using Euclidean distance
4. **Graph Construction** — `route_api.py` builds a weighted graph where edges represent real distances between adjacent stations on the same line
5. **Pathfinding** — Dijkstra's algorithm computes the shortest path between the two nearest stations
6. **Output** — The complete route is printed, including the origin, nearest stations, and destination

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- Required packages:
  ```bash
  pip install pandas requests beautifulsoup4
