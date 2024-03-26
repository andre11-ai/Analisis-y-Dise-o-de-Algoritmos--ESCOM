#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Definición de un punto en el plano
typedef struct{
    double x;
    double y;
} Point;

// Función para encontrar el área signada de un triángulo formado por 3 puntos
double area_sign(Point p1, Point p2, Point p3){
    return (p1.x - p3.x) * (p2.y - p3.y) - (p2.x - p3.x) * (p1.y - p3.y);
}

// Función para imprimir un punto
void print_point(Point p){
    printf("(%f, %f)\n", p.x, p.y);
}

// Función para encontrar los puntos más alejados de una línea
void find_hull_points(Point* points, int n, Point p1, Point p2, double side, Point* hull, int* hull_count){
    double max_dist = 0;
    Point max_point;
    for (int i = 0; i < n; i++){
        double dist = area_sign(p1, p2, points[i]);
        if (dist * side > 0) {
            if (dist > max_dist) {
                max_dist = dist;
                max_point = points[i];
            }
        }
    }
    if (max_dist > 0){
        hull[(*hull_count)++] = max_point;
        find_hull_points(points, n, p1, max_point, -area_sign(p1, max_point, p2), hull, hull_count);
        find_hull_points(points, n, max_point, p2, -area_sign(max_point, p2, p1), hull, hull_count);
    }
}

// Algoritmo Quick Hull
void quick_hull(Point* points, int n){
    if (n < 3){
        printf("Not enough points for convex hull.\n");
        return;
    }

    // Encontrar los puntos extremos
    Point min_x = points[0];
    Point max_x = points[0];
    for (int i = 1; i < n; i++){
        if (points[i].x < min_x.x){
            min_x = points[i];
        }
        if (points[i].x > max_x.x){
            max_x = points[i];
        }
    }

    // Inicializar el arreglo de puntos de la envolvente convexa
    Point hull[2*n]; // El tamaño máximo es 2*n
    int hull_count = 0;
    hull[hull_count++] = min_x;
    hull[hull_count++] = max_x;

    // Encontrar los puntos más alejados de la línea formada por los extremos
    find_hull_points(points, n, min_x, max_x, -1, hull, &hull_count);
    find_hull_points(points, n, max_x, min_x, -1, hull, &hull_count);

    // Imprimir los puntos de la envolvente convexa
    printf("Convex Hull Points:\n");
    for (int i = 0; i < hull_count; i++){
        print_point(hull[i]);
    }
}

int main(){
    clock_t start, end;
    double cpu_time_used;

    // Semilla para la generación de números aleatorios
    srand(time(NULL));

    // Generar n puntos aleatorios
    int n = 10;
    Point points[n];
    for (int i = 0; i < n; i++){
        points[i].x = (double)rand() / RAND_MAX * 1000; // Coordenada x aleatoria en el rango [0, 100]
        points[i].y = (double)rand() / RAND_MAX * 1000; // Coordenada y aleatoria en el rango [0, 100]
    }

    // Calcular el tiempo de inicio
    start = clock();

    // Calcular la envolvente convexa
    quick_hull(points, n);

    // Calcular el tiempo de fin
    end = clock();
    cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;
    printf("Tiempo de ejecución: %f segundos\n", cpu_time_used);

    return 0;
}