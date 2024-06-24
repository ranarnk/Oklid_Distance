# Noktaların tanımlanması
points = [(1, 2), (3, 4), (5, 6), (7, 8)]  # Örnek noktalar


# Öklid Mesafesi için bir fonksiyon yazma
def euclideanDistance(point1, point2):
    return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)**0.5


# Mesafelerin hesaplanması
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distances.append(euclideanDistance(points[i], points[j]))

# Minimum mesafenin bulunması
min_distance = min(distances)
print(f"Minimum Öklid Mesafesi: {min_distance}")
