from django.shortcuts import render
from django.db import connection
import csv
from django.http import HttpResponse

def obtener_datos():
    with connection.cursor() as cursor:
        cursor.execute("""
        SELECT 
            a.docente_id,
            c.nombre,
            c.grupo,
            r.tipo_id,
            r.fecha_limite,
            e.drive_file_id,
            e.created_at,
            CASE 
                WHEN e.id IS NULL THEN 'NO_ENTREGADO'
                WHEN e.created_at <= r.fecha_limite THEN 'A_TIEMPO'
                ELSE 'TARDE'
            END AS estado
        FROM asignaciones a
        JOIN cursos c ON c.id = a.curso_id
        JOIN reglas_entregas r ON r.semestre = c.semestre
        LEFT JOIN entregas e 
            ON e.curso_id = c.id
            AND e.tipo_id = r.tipo_id
            AND e.docente_id = a.docente_id
        """)
        cols=[col[0] for col in cursor.description]
        return [dict(zip(cols,row)) for row in cursor.fetchall()]

def calcular_kpis(datos):
    return {
        'total':len(datos),
        'a_tiempo':sum(1 for d in datos if d['estado']=='A_TIEMPO'),
        'tarde':sum(1 for d in datos if d['estado']=='TARDE'),
        'no_entregado':sum(1 for d in datos if d['estado']=='NO_ENTREGADO')
    }

def dashboard(request):
    datos=obtener_datos()
    kpis=calcular_kpis(datos)
    return render(request,'dashboard.html',{'datos':datos,'kpis':kpis})

def exportar_csv(request):
    datos=obtener_datos()
    response=HttpResponse(content_type='text/csv')
    response['Content-Disposition']='attachment; filename="reporte.csv"'
    writer=csv.writer(response)
    writer.writerow(['docente','curso','tipo','estado'])
    for d in datos:
        writer.writerow([d['docente_id'],d['nombre'],d['tipo_id'],d['estado']])
    return response
