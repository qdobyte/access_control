from rest_framework import viewsets
from rest_framework.response import Response
from django.db import connection


class ReportViewSet(viewsets.ModelViewSet):
    def list(self, request):
        inside_query = """
        SELECT 
            (SELECT COUNT(*) FROM visitors_ingress WHERE is_inside = true) AS visitantes_dentro, 
            (SELECT COUNT(*) FROM employees_ingress WHERE is_inside = true) AS empleados_dentro,
            (SELECT COUNT(*) FROM visitors_ingress WHERE is_inside = true) + 
                (SELECT COUNT(*) FROM employees_ingress WHERE is_inside = true) AS total_personas_dentro;
        """
        with connection.cursor() as cursor:
            cursor.execute(inside_query)
            row = cursor.fetchall()

            report_inside = []

            for r in row:
                report_inside.append({
                    'visitantes_dentro': r[0],
                    'empleados_dentro': r[1],
                    'total_personas_dentro': r[2]
                })

            data = {
                'report_inside': report_inside
            }

        return Response(data)


class ReportEmployeeViewSet(viewsets.ModelViewSet):
    def list(self, request):
        fecha_inicial = request.GET.get('fecha_inicial')
        fecha_final = request.GET.get('fecha_final')

        with connection.cursor() as cursor:
            cursor.callproc('generar_reporte_horas_trabajadas', [fecha_inicial, fecha_final])
            results = cursor.fetchall()

            reporte = []
            for row in results:
                reporte.append({
                    'first_name': row[0],
                    'last_name': row[1],
                    'cost_department': row[2],
                    'horas_trabajadas': str(row[3])
                })

            data = {
                'reporte_horas_trabajadas': reporte
            }

        return Response(data)
