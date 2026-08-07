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
  ```

### Usage

Run the main script and follow the prompts:

```bash
python main_search.py
```

Example interaction:
```
请输入出发点(注意要用简体中文):香港国际机场
请输入终点(注意要用简体中文):铜锣湾
离出发点香港国际机场最近的地鐵站為机场站，离终点铜锣湾最近的地鐵站為铜锣湾站
從香港国际机场=>铜锣湾的最短路徑為['香港国际机场', '机场站', '青衣站', '奥运站', '南昌站', '香港站', '中环站', '金钟站', '铜锣湾站']
```

---

## 🔑 API Key

This project uses the [AMap (高德地图) Web Service API](https://lbs.amap.com/) for geocoding and distance calculations. The API key is hardcoded in the source files:

- `route_api.py` — for distance calculation between stations
- `route_find.py` — for coordinate lookup

> ⚠️ **Note:** For production use, consider moving the API key to an environment variable or configuration file.

---

## 📊 Data Source

The `subway.csv` file contains Hong Kong MTR station data including:
- `name` — Station name
- `site` — Line name (e.g., 港岛线, 观塘线)
- `longitude` / `latitude` — GPS coordinates
- `city` — City name (香港)

The original data was scraped from [MapBar](https://ditie.mapbar.com/hongkong_line/) (see commented code in `route_find.py`).

---

## 🧮 Algorithm

**Dijkstra's Algorithm** is used to find the shortest path in the station graph:

- **Nodes** — MTR stations
- **Edges** — Connections between adjacent stations on the same line
- **Weights** — Real-world distances (in meters) fetched from AMap API

The algorithm guarantees the optimal (shortest distance) route between any two stations in the network.

---

## 📝 Notes

- Location inputs must be in **Simplified Chinese** (简体中文)
- The tool assumes the user walks to the nearest station and then travels entirely by subway
- Transfer stations (stations serving multiple lines) are handled naturally by the graph structure

---

## 📄 License

This project is open source. Feel free to use, modify, and distribute.

---

## 🙋‍♂️ Author

[Dyeus-wwww](https://github.com/Dyeus-wwww)

