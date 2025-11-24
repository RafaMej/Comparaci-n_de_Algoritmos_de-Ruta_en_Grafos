# Comparación de Algoritmos de Rutas en Grafos
Este proyecto implementa y compara tres algoritmos clásicos para búsqueda de
rutas óptimas en grafos ponderados sin pesos negativos:
- Dijkstra
- A* (con heurística admisible)
- Búsqueda de costo uniforme

## Estructura
data/ # Generación de grafos de prueba
src/ # Implementación de algoritmos
experiments/ # Scripts para ejecutar pruebas masivas

## Requisitos
pip install -r requirements.txt

## Generar gráficos
Desde la carpeta `data/`:
python generate_graph.py

## Ejecutar pruebas
Desde `experiments/`:
python run_experiments.py

Los resultados se guardan en:
experiments/results.csv

## Métricas recolectadas
- Tiempo total de ejecución
- Número de expansiones (nodos visitados)
- Costo total del camino

Listo para análisis en el reporte PDF.
