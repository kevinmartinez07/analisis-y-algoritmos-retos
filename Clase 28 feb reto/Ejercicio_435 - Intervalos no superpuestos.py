from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Estrategia greedy:
        # Ordeno los intervalos por su fin para ir escogiendo primero el que termina más rápido. 
        # Si el siguiente no se cruza con el último que dejé, lo conservo. Así puedo dejar la mayor 
        # cantidad de intervalos sin superposición.
        # La respuesta es los que sobran: total - conservados.
        #
        # Complejidad:
        # Tiempo: O(n log n) por el ordenamiento
        # Espacio extra: O(1) sin contar el ordenamiento interno

        if len(intervals) <= 1:
            return 0

        intervals.sort(key=lambda x: x[1])

        kept = 1
        last_end = intervals[0][1]

        for i in range(1, len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]

            if start >= last_end:
                kept += 1
                last_end = end

        return len(intervals) - kept