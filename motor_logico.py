import pandas as pd

def aplicar_reglas_compartidas(nombre_materia, carrera, plan, mats, horas, aca):
    m_res, h_res, a_res = mats, horas, aca
    
    # 1. Matemática para informática I
    if nombre_materia == "Matemática para informática I":
        if plan != "2018":
            m_res -= 1
            h_res -= 64

   # 2. Matemática para informática II
    elif nombre_materia == "Matemática para informática II":
        # Caso Licenciatura 2018 (128hs)
        if plan == "2018" and "Licenciatura en Informática" in carrera:
            m_res -= 1
            h_res -= 128
        
        elif plan == "2022" and "Tecnicatura en Videojuegos" in carrera:
            m_res -= 1
            h_res -= 96
        # Casos que descuentan 64hs y 1 materia:
        elif (
            (plan == "2025" and "Licenciatura en Informática" in carrera) or
            (plan == "2022" and "Tecnicatura en Programación" in carrera) or
            (plan == "2025" and "Tecnicatura en Programación" in carrera) or
            (plan == "2022" and "Tecnicatura en Redes" in carrera) or
            (plan == "2025" and "Licenciatura en Ciberseguridad" in carrera) or
            (plan == "2025" and "Licenciatura en Videojuegos" in carrera)
        ):
            m_res -= 1
            h_res -= 64
        
        # El resto de los casos (Redes 2025, Videojuegos Tec. 2025, IA) 
        # no entran en ninguna condición, por lo tanto m_res y h_res quedan igual.

    # 3. Introducción a Logica y Problemas Computacionales
    elif nombre_materia == "Introducción a Logica y Problemas Computacionales":
        if plan != "2018":
            m_res -= 1
            h_res -= 64

    # 4. Programación Estructurada
    elif nombre_materia == "Programación Estructurada":
        if plan == "2018":
            m_res -= 1
            h_res -= 128
        elif ((plan == "2025" and "Tecnicatura en Programación" in carrera) or 
              (plan == "2022" and "Tecnicatura en Programación" in carrera) or 
              (plan == "2025" and "Licenciatura en Informática" in carrera) or 
              (plan == "2022" and "Tecnicatura en Videojuegos" in carrera)):
            m_res -= 1
            h_res -= 96
        else:
            m_res -= 1
            h_res -= 64

   # 5. Organización de Computadoras I
    elif nombre_materia == "Organización de Computadoras I":
        # Caso específico: Tecnicatura en Programación 2022 (96hs)
        if plan == "2022" and "Tecnicatura en Programación" in carrera:
            m_res -= 1
            h_res -= 96
        
        # Casos que descuentan 64hs y 1 materia:
        elif (
            (plan == "2025" and "Licenciatura en Informática" in carrera) or
            (plan == "2025" and "Tecnicatura en Programación" in carrera) or
            (plan == "2022" and "Tecnicatura en Redes" in carrera) or
            (plan == "2025" and "Tecnicatura en Redes" in carrera) or
            (plan == "2025" and "Licenciatura en Ciberseguridad" in carrera)
        ):
            m_res -= 1
            h_res -= 64

        # Todos los demás casos (Lic. 2018, Videojuegos e Inteligencia Artificial)
        # no entran en las condiciones, por lo tanto "no tienen efecto".

   # 6. Organización de Computadoras II
    elif nombre_materia == "Organización de Computadoras II":
        # Casos que descuentan 96hs y 1 materia:
        if (
            (plan == "2018" and "Licenciatura en Informática" in carrera) or
            (plan == "2022" and "Tecnicatura en Redes" in carrera)
        ):
            m_res -= 1
            h_res -= 96
        
        # Casos que descuentan 64hs y 1 materia:
        elif (
            (plan == "2025" and "Licenciatura en Informática" in carrera) or
            (plan == "2022" and "Tecnicatura en Programación" in carrera) or
            (plan == "2025" and "Tecnicatura en Redes" in carrera) or
            (plan == "2025" and "Licenciatura en Ciberseguridad" in carrera)
        ):
            m_res -= 1
            h_res -= 64

        # El resto (Tec. Programación 2025, Videojuegos, IA) no entra en los IF,
        # cumpliendo con que "no tiene efecto".

    # 7. Programación con Objetos I
    elif nombre_materia == "Programación con Objetos I":
        # Casos que descuentan 128hs y 1 materia (Planes viejos)
        if (
            (plan == "2018" and "Licenciatura en Informática" in carrera) or
            (plan == "2022" and "Tecnicatura en Programación" in carrera) or
            (plan == "2022" and "Tecnicatura en Videojuegos" in carrera)
        ):
            m_res -= 1
            h_res -= 128
        
        # Casos que descuentan 96hs y 1 materia (Planes nuevos)
        elif (
            (plan == "2025" and "Licenciatura en Informática" in carrera) or
            (plan == "2025" and "Tecnicatura en Programación" in carrera) or
            (plan == "2025" and "Tecnicatura en Videojuegos" in carrera) or
            (plan == "2025" and "Licenciatura en Videojuegos" in carrera)
        ):
            m_res -= 1
            h_res -= 96

        # Redes, Ciberseguridad e Inteligencia Artificial no entran en los IF,
        # por lo que no tienen efecto (m_res y h_res quedan igual).

   # 8. Bases de Datos
    elif nombre_materia == "Bases de Datos":
        # Esta materia afecta a TODAS las carreras informática de la UNahur
        # Bloque de planes "viejos" (96hs)
        if plan in ["2018", "2022", "2023"]:
            m_res -= 1
            h_res -= 96
        
        # Bloque de planes nuevos / 2025 (64hs)
        elif plan == "2025":
            m_res -= 1
            h_res -= 64

    # 9. Redes de Computadoras
    elif nombre_materia == "Redes de Computadoras":
        # Caso especial: Inteligencia Artificial 2025 (Créditos ACA)
        if plan == "2025" and "Inteligencia Artificial" in carrera:
            a_res -= 4
        
        # Casos que descuentan 96hs (Planes viejos)
        elif (
            (plan == "2018" and "Licenciatura en Informática" in carrera) or
            (plan == "2022" and "Tecnicatura en Redes" in carrera)
        ):
            m_res -= 1
            h_res -= 96
            
        # Casos que descuentan 64hs (Planes nuevos o IA 2023)
        elif (
            (plan == "2025" and "Licenciatura en Informática" in carrera) or
            (plan == "2022" and "Licenciatura en Informática" in carrera) or
            (plan == "2022" and "Tecnicatura en Programación" in carrera) or
            (plan == "2025" and "Tecnicatura en Redes" in carrera) or
            (plan == "2025" and "Licenciatura en Ciberseguridad" in carrera) or
            (plan == "2023" and "Inteligencia Artificial" in carrera)
        ):
            m_res -= 1
            h_res -= 64

        # El resto (Programación y Videojuegos) no entran en ningún IF,
        # así que no tienen efecto.

    # 10. Construcción de Interfaces de Usuario
    elif nombre_materia == "Construccion de Interfaces de Usuario":
        # Casos que descuentan 96hs y 1 materia (Planes viejos)
        if (
            (plan == "2018" and "Licenciatura en Informática" in carrera) or
            (plan == "2022" and "Tecnicatura en Programación" in carrera) or
            (plan == "2022" and "Tecnicatura en Videojuegos" in carrera)
        ):
            m_res -= 1
            h_res -= 96
        
        # Casos que descuentan 64hs y 1 materia (Planes nuevos 2025)
        elif (
            (plan == "2025" and "Licenciatura en Informática" in carrera) or
            (plan == "2025" and "Tecnicatura en Programación" in carrera) or
            (plan == "2025" and "Tecnicatura en Videojuegos" in carrera) or
            (plan == "2025" and "Licenciatura en Videojuegos" in carrera)
        ):
            m_res -= 1
            h_res -= 64

        # Redes, Ciberseguridad e Inteligencia Artificial quedan fuera de los IF,
        # cumpliendo con que "no tiene efecto".

    # 11. Elementos de Ingeniería de Software
    elif nombre_materia == "Elementos de Ingeniería de Software":
        # Casos que descuentan 128hs (El gran salto del Plan 2025)
        if plan == "2025" and ("Licenciatura en Informática" in carrera or "Tecnicatura en Programación" in carrera):
            m_res -= 2
            h_res -= 128
        
        # Casos que descuentan 96hs (Planes viejos)
        elif (
            (plan == "2018" and "Licenciatura en Informática" in carrera) or
            (plan == "2022" and "Tecnicatura en Programación" in carrera) or
            (plan == "2022" and "Tecnicatura en Videojuegos" in carrera)
        ):
            m_res -= 1
            h_res -= 96
            
        # Casos que descuentan 64hs (Videojuegos Plan 2025)
        elif plan == "2025" and ("Tecnicatura en Videojuegos" in carrera or "Licenciatura en Videojuegos" in carrera):
            m_res -= 1
            h_res -= 64

        # Redes, Ciber e IA quedan fuera, cumpliendo con que "no tiene efecto".

    # 12. Sistemas Operativos
    elif nombre_materia == "Sistemas Operativos":
        # Casos que descuentan 96hs (Planes viejos)
        if (
            (plan == "2018" and "Licenciatura en Informática" in carrera) or
            (plan == "2022" and "Tecnicatura en Redes" in carrera)
        ):
            m_res -= 1
            h_res -= 96
        
        # Casos que descuentan 64hs (Planes nuevos 2025)
        elif (
            (plan == "2025" and "Licenciatura en Informática" in carrera) or
            (plan == "2025" and "Tecnicatura en Redes" in carrera) or
            (plan == "2025" and "Licenciatura en Ciberseguridad" in carrera)
        ):
            m_res -= 1
            h_res -= 64

        # Programación, Videojuegos e Inteligencia Artificial quedan fuera,
        # así que no tienen efecto (m_res y h_res se mantienen).

    # 13. Tecnología y Sociedad
    elif nombre_materia == "Tecnología y Sociedad":
        # Casos que descuentan 48hs (Planes anteriores)
        if (
            (plan == "2018" and "Licenciatura en Informática" in carrera) or
            (plan == "2023" and "Tecnicatura en Inteligencia Artificial" in carrera)
        ):
            m_res -= 1
            h_res -= 48
        
        # Casos que descuentan 64hs (Plan 2025 y nuevas Licenciaturas)
        elif (
            (plan == "2025" and "Licenciatura en Informática" in carrera) or
            (plan == "2025" and "Licenciatura en Ciberseguridad" in carrera) or
            (plan == "2025" and "Licenciatura en Videojuegos" in carrera) or
            (plan == "2025" and "Tecnicatura en Inteligencia Artificial" in carrera)
        ):
            m_res -= 1
            h_res -= 64

        # Programación, Redes y Tec. en Videojuegos no entran en los IF,
        # por lo que no tienen efecto (m_res y h_res quedan igual).

        # --- MATERIAS ESPECÍFICAS DE REDES ---

    # 14. Sistemas de comunicación
    elif nombre_materia == "Sistemas de comunicación":
        if plan == "2025" and ("Tecnicatura en Redes" in carrera or "Licenciatura en Ciberseguridad" in carrera):
            m_res -= 1
            h_res -= 96
        elif plan == "2022" and "Tecnicatura en Redes" in carrera:
            m_res -= 1
            h_res -= 64

    # 15. Taller de intérpretes de comandos
    elif nombre_materia == "Taller de intérpretes de comandos":
        if ("Tecnicatura en Redes" in carrera or "Licenciatura en Ciberseguridad" in carrera):
            m_res -= 1
            h_res -= 64

    # 16. Operaciones I
    elif nombre_materia == "Operaciones I":
        if ("Tecnicatura en Redes" in carrera or "Licenciatura en Ciberseguridad" in carrera):
            m_res -= 1
            h_res -= 64

    # 17. Operaciones II
    elif nombre_materia == "Operaciones II":
        if ("Tecnicatura en Redes" in carrera or "Licenciatura en Ciberseguridad" in carrera):
            m_res -= 1
            h_res -= 96

    # 18. Redes avanzadas
    elif nombre_materia == "Redes avanzadas":
        if ("Tecnicatura en Redes" in carrera or "Licenciatura en Ciberseguridad" in carrera):
            m_res -= 1
            h_res -= 96

    # --- MATERIAS ESPECÍFICAS DE VIDEOJUEGOS ---

    # 19. Introducción a los Videojuegos
    elif nombre_materia == "Introducción a los Videojuegos":
        if plan == "2025" and ("Tecnicatura en Videojuegos" in carrera or "Licenciatura en Videojuegos" in carrera):
            m_res -= 1
            h_res -= 96
        elif plan == "2022" and "Tecnicatura en Videojuegos" in carrera:
            m_res -= 1
            h_res -= 64

    # 20. Arte digital para videojuegos
    elif nombre_materia == "Arte digital para videojuegos":
        if "Videojuegos" in carrera:
            m_res -= 1
            h_res -= 64

    # 21. Taller de diseño conceptual de juegos
    elif nombre_materia == "Taller de diseño conceptual de juegos":
        if plan == "2022" and "Tecnicatura en Videojuegos" in carrera:
            m_res -= 1
            h_res -= 96
        elif plan == "2025" and ("Tecnicatura en Videojuegos" in carrera or "Licenciatura en Videojuegos" in carrera):
            m_res -= 1
            h_res -= 64

    # 22. Introducción a motores de videojuegos
    elif nombre_materia == "Introducción a motores de videojuegos":
        if "Videojuegos" in carrera:
            m_res -= 1
            h_res -= 64

    # 23. Programación de videojuegos I
    elif nombre_materia == "Programación de videojuegos I":
        if plan == "2022" and "Tecnicatura en Videojuegos" in carrera:
            m_res -= 1
            h_res -= 96
        elif plan == "2025" and ("Tecnicatura en Videojuegos" in carrera or "Licenciatura en Videojuegos" in carrera):
            m_res -= 1
            h_res -= 64

    # 24. Programación de videojuegos II
    elif nombre_materia == "Programación de videojuegos II":
        if "Videojuegos" in carrera:
            m_res -= 1
            h_res -= 96

    # 25. Diseño Lúdico
    elif nombre_materia == "Diseño Lúdico":
        if (plan == "2022" and "Tecnicatura en Videojuegos" in carrera) or \
           (plan == "2025" and "Licenciatura en Videojuegos" in carrera):
            m_res -= 1
            h_res -= 64
        # Tecnicatura 2025 no tiene efecto según tu lista

    # 26. Planificación de negocios
    elif nombre_materia == "Planificación de negocios":
        if plan == "2025" and ("Tecnicatura en Videojuegos" in carrera or "Licenciatura en Videojuegos" in carrera):
            m_res -= 1
            h_res -= 64

    #IA----------------------------------------
    # --- MATERIAS ESPECÍFICAS DE INTELIGENCIA ARTIFICIAL ---

   # 27. Taller de programación II
    elif nombre_materia == "Taller de programación II":
        # Solo tiene efecto en la Tecnicatura en IA (ambos planes)
        if "Inteligencia Artificial" in carrera:
            m_res -= 1
            h_res -= 64

    # 27. Taller de programación II
    elif nombre_materia == "Taller de programación III":
        # Solo tiene efecto en la Tecnicatura en IA (ambos planes)
        if "Inteligencia Artificial" in carrera:
            m_res -= 1
            h_res -= 64
    
    elif nombre_materia == "Introducción a la inteligencia artificial":
        # Solo tiene efecto en la Tecnicatura en IA (ambos planes)
        if "Inteligencia Artificial" in carrera:
            m_res -= 1
            h_res -= 64

    elif nombre_materia == "Álgebra lineal":
        if plan == "2025" and "Licenciatura en Informática" in carrera:
            m_res -= 1
            h_res -= 64
        elif "Inteligencia Artificial" in carrera:
            m_res -= 1
            h_res -= 64

    # 28. Cálculo
    elif nombre_materia == "Cálculo":
        if plan == "2025" and "Inteligencia Artificial" in carrera:
            m_res -= 1
            h_res -= 96
        elif plan == "2023" and "Inteligencia Artificial" in carrera:
            m_res -= 1
            h_res -= 64

    # 29. Fundamentos de ciencias de datos
    elif nombre_materia == "Fundamentos de ciencias de datos":
        if plan == "2025" and "Inteligencia Artificial" in carrera:
            m_res -= 1
            h_res -= 64
        elif plan == "2023" and "Inteligencia Artificial" in carrera:
            m_res -= 1
            h_res -= 48

    #fundamentos de redes neuronales
    # 28. Fundamentos Redes Neuronales
    elif nombre_materia == "Fundamentos Redes Neuronales":
        # Descuenta en IA (ambos planes) y en la Licenciatura en Informática 2025
        if ("Inteligencia Artificial" in carrera) or \
           (plan == "2025" and "Licenciatura en Informática" in carrera):
            m_res -= 1
            h_res -= 64

    # 29. Aprendizaje Automático 
    elif nombre_materia == "Aprendizaje Automático":
        # Descuenta 64hs en:
        # - Todos los planes de Inteligencia Artificial
        # - Licenciatura en Informática (tanto Plan 2018 como Plan 2025)
        if ("Inteligencia Artificial" in carrera) or \
           ("Licenciatura en Informática" in carrera):
            m_res -= 1
            h_res -= 64

    # 30. Aprendizaje Automático Avanzado
    elif nombre_materia == "Aprendizaje Automático Avanzado":
        # Caso 1: Inteligencia Artificial (Descuenta 96hs)
        if "Inteligencia Artificial" in carrera:
            m_res -= 1
            h_res -= 96
        
        # Caso 2: Licenciatura en Informática Plan 2018 (Descuenta 64hs)
        elif plan == "2018" and "Licenciatura en Informática" in carrera:
            m_res -= 1
            h_res -= 64

    # 31. Procesamiento de Imágenes y Visión por Computadora
    elif nombre_materia == "Procesamiento de Imágenes y Visión por Computadora":
        if plan == "2023" and "Inteligencia Artificial" in carrera:
            m_res -= 1
            h_res -= 96
        elif plan == "2025" and "Inteligencia Artificial" in carrera:
            m_res -= 1
            h_res -= 64

    # 32. Proyecto integrador
    elif nombre_materia == "Proyecto integrador":
        if plan == "2025" and "Inteligencia Artificial" in carrera:
            m_res -= 1
            h_res -= 96
        elif plan == "2023" and "Inteligencia Artificial" in carrera:
            m_res -= 1
            h_res -= 80

    # Nota: Taller de programación I no tiene efecto.
    # se reciben con probabilidad y estadistica que es de licenciatura en informatica
    # --- MATERIAS DE PROGRAMACIÓN ---

    # 31. Taller de marcado
    elif nombre_materia == "Taller de marcado":
        # Descuenta 64hs en Lic. Informática 2025 y Tec. Programación (2022 y 2025)
        if (plan == "2025" and "Licenciatura en Informática" in carrera) or \
           ("Tecnicatura en Programación" in carrera):
            m_res -= 1
            h_res -= 64

    # 32. Estructuras de Datos
    elif nombre_materia == "Estructuras de Datos":
        # Planes viejos (2018 / 2022) descuentan 128hs
        if (plan == "2018" and "Licenciatura en Informática" in carrera) or \
           (plan == "2022" and "Tecnicatura en Programación" in carrera):
            m_res -= 1
            h_res -= 128
        # Planes nuevos (2025) descuentan 96hs
        elif plan == "2025" and ("Licenciatura en Informática" in carrera or "Tecnicatura en Programación" in carrera):
            m_res -= 1
            h_res -= 96

    # 33. Programación con Objetos II
    elif nombre_materia == "Programación con Objetos II":
        # Descuenta 96hs en todos los planes de Lic. Informática y Tec. Programación
        if ("Licenciatura en Informática" in carrera) or ("Tecnicatura en Programación" in carrera):
            m_res -= 1
            h_res -= 96

    # 34. Programación Concurrente
    elif nombre_materia == "Programación Concurrente":
        # Descuenta 64hs en Lic. Informática (ambos), Tec. Prog 2022 y Ciberseguridad 2025
        if ("Licenciatura en Informática" in carrera) or \
           (plan == "2022" and "Tecnicatura en Programación" in carrera) or \
           (plan == "2025" and "Licenciatura en Ciberseguridad" in carrera):
            m_res -= 1
            h_res -= 64
        # Tecnicatura en Programación 2025 queda afuera (no tiene efecto)

    # 35. Programación Funcional
    elif nombre_materia == "Programación Funcional":
        # Caso plan viejo: Lic. Informática 2018 (descuenta 64hs reloj)
        if plan == "2018" and "Licenciatura en Informática" in carrera:
            m_res -= 1
            h_res -= 64
            
        # Caso planes nuevos: Lic. Informática 2025 y Tec. Programación 2025 (descuenta 5 créditos ACA)
        elif plan == "2025" and ("Licenciatura en Informática" in carrera or "Tecnicatura en Programación" in carrera):
            a_res -= 5
            
        # Caso Tecnicatura en Programación 2022 con condicional cruzada
       # elif plan == "2022" and "Tecnicatura en Programación" in carrera:
            # "SINO tiene aprobada Programación Concurrente, descuenta..."
          #  if "Programación Concurrente" not in materias_aprobadas:
           #     m_res -= 1
            #    h_res -= 64
            # Si está en la lista, entra en el else implícito (no tiene efecto)

    # 36. Estrategias de Persistencia
    elif nombre_materia == "Estrategias de Persistencia":
        # Planes viejos (2018 / 2022) descuentan 96hs
        if (plan == "2018" and "Licenciatura en Informática" in carrera) or \
           (plan == "2022" and "Tecnicatura en Programación" in carrera):
            m_res -= 1
            h_res -= 96
        # Planes nuevos (2025) descuentan 64hs
        elif plan == "2025" and ("Licenciatura en Informática" in carrera or "Tecnicatura en Programación" in carrera):
            m_res -= 1
            h_res -= 64

    # 37. Sist Inf Geografica (Electiva)
    elif nombre_materia == "Sist Inf Geografica (Electiva)":
        # Solo afecta a los planes nuevos (2025) descontando 5 créditos ACA
        if plan == "2025" and ("Licenciatura en Informática" in carrera):
            a_res -= 4
        elif plan == "2025" and ("Tecnicatura en Programación" in carrera):
            a_res -= 3

    # --- MATERIAS DE LA LICENCIATURA EN INFORMÁTICA ---

    # 38. Algoritmos
    elif nombre_materia == "Algoritmos":
        if plan == "2018" and "Licenciatura en Informática" in carrera:
            m_res -= 1
            h_res -= 96
        elif plan == "2025" and "Licenciatura en Informática" in carrera:
            m_res -= 1
            h_res -= 64

    # 39. Laboratorio de Sistemas Op. y Redes
    elif nombre_materia == "Laboratorio de Sistemas Op. y Redes":
        if "Licenciatura en Informática" in carrera or "Licenciatura en Ciberseguridad" in carrera:
            m_res -= 1
            h_res -= 64
        elif plan == "2022" and "Tecnicatura en Redes" in carrera:
            m_res -= 1
            h_res -= 96

    # 40. Lógica y Programación
    elif nombre_materia == "Lógica y Programación":
        if "Licenciatura en Informática" in carrera:
            m_res -= 1
            h_res -= 96

    # 41. Programación con Objetos III
    elif nombre_materia == "Programación con Objetos III":
        if plan == "2018" and "Licenciatura en Informática" in carrera:
            m_res -= 1
            h_res -= 96
        elif plan == "2025" and ("Licenciatura en Informática" in carrera or "Tecnicatura en Programación" in carrera):
            a_res -= 5

    # 42. Seguridad de la Información
    elif nombre_materia == "Seguridad de la Información":
        if "Licenciatura en Informática" in carrera or "Licenciatura en Ciberseguridad" in carrera:
            m_res -= 1
            h_res -= 64
        elif "Tecnicatura en Redes" in carrera:
            m_res -= 1
            h_res -= 96 if plan == "2022" else 64

    # 43. Análisis Matemático
    elif nombre_materia == "Análisis Matemático":
        if "Licenciatura en Informática" in carrera:
            m_res -= 1
            h_res -= 96 if plan == "2018" else 64

    # 44. Matemática II
    elif nombre_materia == "Matemática II":
        if "Licenciatura en Informática" in carrera or "Inteligencia Artificial" in carrera:
            m_res -= 1
            h_res -= 64

    # 45. Matemática III
    elif nombre_materia == "Matemática III":
        if "Licenciatura en Informática" in carrera:
            m_res -= 1
            h_res -= 64

    # 46. Probabilidad y Estadística
    elif nombre_materia == "Probabilidad y Estadística":
        if "Licenciatura en Informática" in carrera or "Inteligencia Artificial" in carrera:
            m_res -= 1
            h_res -= 96

    # 47. Ingeniería de Requerimientos
    elif nombre_materia == "Ingeniería de Requerimientos":
        if "Licenciatura en Informática" in carrera:
            m_res -= 1
            h_res -= 96

    # 48. Desarrollo de Aplicaciones
    elif nombre_materia == "Desarrollo de Aplicaciones":
        if "Licenciatura en Informática" in carrera:
            m_res -= 1
            h_res -= 96 if plan == "2018" else 64

    # 49. Gestión de Proyectos de Des. de Software
    elif nombre_materia == "Gestión de Proyectos de Des. de Software":
        if "Licenciatura en Informática" in carrera:
            m_res -= 1
            h_res -= 64

    # 50. Práctica Profesional Supervisada (PPS)
    elif nombre_materia == "Práctica Profesional Supervisada (PPS)":
        if ("Licenciatura en Informática" in carrera) or \
           (plan == "2025" and ("Licenciatura en Ciberseguridad" in carrera or "Licenciatura en VideoJuegos" in carrera)):
            m_res -= 1
            h_res -= 64

    # 51. Teorías de la Computación
    elif nombre_materia == "Teorías de la Computación":
        if "Licenciatura en Informática" in carrera:
            m_res -= 1
            h_res -= 64

    # 52. Arquitectura de SW I
    elif nombre_materia == "Arquitectura de SW I":
        if "Licenciatura en Informática" in carrera:
            m_res -= 1
            h_res -= 64

    # 53. Sistemas Distribuidos y Tiempos Real
    elif nombre_materia == "Sistemas Distribuidos y Tiempos Real":
        if "Licenciatura en Informática" in carrera:
            m_res -= 1
            h_res -= 96 if plan == "2018" else 64

    # 54. Lenguajes Formales y Autómatas
    elif nombre_materia == "Lenguajes Formales y Autómatas":
        if plan == "2018" and "Licenciatura en Informática" in carrera:
            m_res -= 1
            h_res -= 64
        elif plan == "2025" and "Licenciatura en Informática" in carrera:
            a_res -= 5
        elif plan == "2025" and "Tecnicatura en Programación" in carrera:
            a_res -= 3

    # 55. Características de Lenguajes de Comp.
    elif nombre_materia == "Características de Lenguajes de Comp.":
        if plan == "2018" and "Licenciatura en Informática" in carrera:
            m_res -= 1
            h_res -= 64
        elif plan == "2025" and "Licenciatura en Informática" in carrera:
            # Solo suma 5 créditos si NO tiene aprobada "Parseo y Generación de Código"
            a_res += 5

    # 56. Arquitectura de SW II
    elif nombre_materia == "Arquitectura de SW II":
        if "Licenciatura en Informática" in carrera:
            m_res -= 1
            h_res -= 64

    # 57. Arquitectura de Computadoras
    elif nombre_materia == "Arquitectura de Computadoras":
        if "Licenciatura en Informática" in carrera:
            m_res -= 1
            h_res -= 64

   # 58. Parseo y Generación de Código
    elif nombre_materia == "Parseo y Generación de Código":
        if "Licenciatura en Informática" in carrera:
            m_res -= 1
            h_res -= 64
            # Si está en el plan 2025 y además tiene aprobada "Características de Lenguajes de Comp.", resta 5 créditos ACA
            if plan == "2025" and "Características de Lenguajes de Comp." in "materias_aprobadas":
                a_res -= 5

    # 59. Ejercicio Profesional
    elif nombre_materia == "Ejercicio Profesional":
        if "Licenciatura en Informática" in carrera:
            m_res -= 1
            h_res -= 48 if plan == "2018" else 64

    # 60. Tesina de Licenciatura
    elif nombre_materia == "Tesina de Licenciatura":
        if "Licenciatura en Informática" in carrera:
            m_res -= 1
            h_res -= 160 if plan == "2018" else 96

    # 61. Materia Optativa 1 (no Ap. Automático ni Redes Neur.)
    elif nombre_materia == "Materia Optativa 1 (no Ap. Automático ni Redes Neur.)":
        if plan == "2018" and "Licenciatura en Informática" in carrera:
            m_res -= 1
            h_res -= 64
        elif plan == "2025" and "Licenciatura en Informática" in carrera:
            a_res -= 4

    # 62. Materia Optativa 2 (no Ap. Automático ni Redes Neur.)
    elif nombre_materia == "Materia Optativa 2 (no Ap. Automático ni Redes Neur.)":
        if plan == "2025" and "Licenciatura en Informática" in carrera:
            a_res -= 4

    # 63. Sistemas y Organizaciones
    elif nombre_materia == "Sistemas y Organizaciones":
        if plan == "2025" and "Licenciatura en Informática" in carrera:
            m_res -= 1
            h_res -= 32

    # --- ACTIVIDADES DE CRÉDITOS: PARTE 1 - ESPACIO DE INTEGRACIÓN CURRICULAR ---

    # 1. Desarrollo de Aplicaciones, en UNAHUR (Prog)
    elif nombre_materia == "Desarrollo de Aplicaciones, en UNAHUR (Prog)":
        if plan == "2025" and "Licenciatura en Informática" in carrera:
            a_res -= 6
        elif "Tecnicatura en Programación" in carrera:
            if plan == "2022":
                a_res -= 20
            elif plan == "2025":
                a_res -= 4

    # 2. Práctica Profesional Supervisada PPS (Prog)
    elif nombre_materia == "Práctica Profesional Supervisada PPS (Prog)":
        if plan == "2025" and "Licenciatura en Informática" in carrera:
            a_res -= 6
        elif "Tecnicatura en Programación" in carrera:
            if plan == "2022":
                a_res -= 20
            elif plan == "2025":
                a_res -= 4

    # 3. Proyecto Integrador (Prog)
    elif nombre_materia == "Proyecto Integrador (Prog)":
        if plan == "2025" and "Licenciatura en Informática" in carrera:
            a_res -= 6
        elif "Tecnicatura en Programación" in carrera:
            if plan == "2022":
                a_res -= 20
            elif plan == "2025":
                a_res -= 4

    # 4. Desarrollo de Aplicaciones, en UNAHUR (Redes)
    elif nombre_materia == "Desarrollo de Aplicaciones, en UNAHUR (Redes)":
        if plan == "2025" and ("Licenciatura en Informática" in carrera or "Licenciatura en Ciberseguridad" in carrera):
            a_res -= 6
        elif "Tecnicatura en Redes" in carrera:
            if plan == "2022":
                a_res -= 20
            elif plan == "2025":
                a_res -= 2

    # 5. Práctica Profesional Supervisada PPS (Redes)
    elif nombre_materia == "Práctica Profesional Supervisada PPS (Redes)":
        if plan == "2025" and ("Licenciatura en Informática" in carrera or "Licenciatura en Ciberseguridad" in carrera):
            a_res -= 6
        elif "Tecnicatura en Redes" in carrera:
            if plan == "2022":
                a_res -= 20
            elif plan == "2025":
                a_res -= 2

    # 6. Proyecto Integrador (Redes)
    elif nombre_materia == "Proyecto Integrador (Redes)":
        if plan == "2025" and ("Licenciatura en Informática" in carrera or "Licenciatura en Ciberseguridad" in carrera):
            a_res -= 6
        elif "Tecnicatura en Redes" in carrera:
            if plan == "2022":
                a_res -= 20
            elif plan == "2025":
                a_res -= 2

    # 7. Proyecto integrador Final (VJ)
    elif nombre_materia == "Proyecto integrador Final (VJ)":
        if plan == "2025" and ("Licenciatura en Informática" in carrera or "Licenciatura en Videojuegos" in carrera):
                a_res -= 6
        elif "Tecnicatura en Videojuegos" in carrera:
                a_res -= 2
        elif plan == "2022" and "Tecnicatura en Videojuegos" in carrera:
            a_res -= 20
            

    # --- ACTIVIDADES DE CRÉDITOS: PARTE 2 - FORMATIVAS ACADÉMICAS Y PROFESIONALES ---

    descuentos_antiguos = {
        # Descuentan 1 en planes viejos (2022/2023)
        "Participación como asistente en Jornadas / Workshops / Congresos - (Evento de 1 día presencial)": 1,
        "Formación Profesional": 1,
        "Formación Profesional (Segunda Participación)": 1,
        "Cómo hacer videojuegos sin volverse loco: Gestión, Diseño y Validación de Usuario": 1,
        "Creación y Animación de Personajes 2D-Del boceto al Sprite Sheet.": 1,
        "Charlas con Graduados": 1,
        "PIA Taller 1": 1,
        "Taller Introductorio de Integrales": 1,
        "Taller de Introducción al procesamiento digital de Imágenes": 1,
        "Git": 1,
        "GraphQL en Springboot": 1,

        # Descuentan 2 en planes viejos (2022/2023)
        "Participación como asistente en Jornadas / Workshops / Congresos": 2,
        "Talleres especiales - Taller de GitHub": 2,
        "Talleres especiales - Taller de Gestión de la seguridad informática": 2,
        "Taller de Procesamiento digital de imágenes": 2,
        "Presentación de nuevos planes de las carreras de informática": 2,
        "Diseño Narrativo de Personajes: Cómo comenzar un relato": 2,
        "Taller de robótica": 2,
        "Curso Introducción al Cómputo Paralelo": 2,
        "De wollok a Java": 2,
        "Taller de programación": 2,
        "Principios básicos de la Seguridad de la Información y la Ciberseguridad": 2,
        "Vibe Coding": 2,
        "Taller de uso de herramientas para el procesamiento de datos": 2,

        # Descuentan 3 en planes viejos (2022/2023)
        "Talleres Especiales - Gestión de Firewall": 3,
        "Participación en Competencias Estudiantiles - Rally Innovación": 3,
        "Participación en competencias estudiantiles": 3,
        "Participación en Proyectos Abiertos": 3,
        "Intercambios estudiantiles presenciales y/o virtuales": 3,
        "Talleres Especiales (más de 32hs)": 3,
        "Curso Project Management": 3,
        "Curso Oracle SQL & PL SQL": 3,
        "Curso Redes Móviles Celulares": 3,
        "Curso Enlaces Inalámbricos Fijos": 3,
        "Curso Redes de Fibra Óptica": 3,
        "Del Prototipo al Portfolio Profesional": 3,
        "Lenguajes educativos para aprender a programar": 3,
        "Curso Introducción a UML": 3,

        # Descuentan 5 en planes viejos (2022/2023)
        "Rally Latinoamericano de Innovación - 1ra participación": 5,
        "Rally Latinoamericano de Innovación - 2da participación": 5,
        "Cursadas Voluntarias en otras Universidades": 5,
    }

    if nombre_materia in descuentos_antiguos:
        # Excepción Licenciatura en Informática 2018: no tiene efecto
        if plan == "2018" and "Licenciatura en Informática" in carrera:
            pass
        # Planes 2025: descuentan 1 por defecto (salvo Cursadas Voluntarias y Talleres >32hs que descuentan 2)
        elif plan == "2025":
            if nombre_materia in ["Cursadas Voluntarias en otras Universidades", "Talleres Especiales (más de 32hs)"]:
                a_res -= 2
            else:
                a_res -= 1
        # Planes 2022 / 2023: aplican el descuento según la tabla
        elif plan in ["2022", "2023"]:
            a_res -= descuentos_antiguos[nombre_materia]


    

    #el eje que absorve los datos 
    return m_res, h_res, a_res

    

    

def calcular_todos_los_progresos(materias_aprobadas):
    df_maestro = pd.read_csv('datos_maestros.csv')
    resultados = []

    for _, row in df_maestro.iterrows():
        carrera = row['carrera']
        plan = str(row['plan'])
        
        mats_restantes = row['total_materias']
        horas_restantes = row['total_horas']
        aca_restante = row['req_total_creditos_aca']

        # --- FASE 1: LÓGICA DE INGLÉS ---
        tiene_ingles_1 = "Inglés I" in materias_aprobadas
        tiene_ingles_2 = "Inglés II" in materias_aprobadas

        if plan in ["2018", "2022", "2023"]:
            if tiene_ingles_1:
                mats_restantes -= 1
                horas_restantes -= 32
            if tiene_ingles_2:
                mats_restantes -= 1
                horas_restantes -= 32

        elif plan == "2025":
            if "Licenciatura en Informática" in carrera:
                if tiene_ingles_1 and not tiene_ingles_2:
                    aca_restante -= 3
                elif tiene_ingles_1 and tiene_ingles_2:
                    mats_restantes -= 1
                    horas_restantes -= 32
            elif "Inteligencia Artificial" in carrera:
                if tiene_ingles_2:
                    mats_restantes -= 1
                    horas_restantes -= 32
            elif "Tecnicatura en Programación" in carrera:
                if tiene_ingles_2:
                    mats_restantes -= 1
                    horas_restantes -= 32
                elif tiene_ingles_1:
                    aca_restante -= 3
            else:
                if tiene_ingles_1: aca_restante -= 3
                if tiene_ingles_2: aca_restante -= 3

        # --- FASE 1.1: MATERIAS UNAHUR Y NUEVOS ENTORNOS ---
        if "Materia UNAHUR I" in materias_aprobadas:
            mats_restantes -= 1
            horas_restantes -= 32
        if "Materia UNAHUR II" in materias_aprobadas:
            if "Licenciatura en Informática" in carrera and plan == "2025":
                aca_restante -= 4
            elif plan == "2018":
                mats_restantes -= 1
                horas_restantes -= 32
        if "Nuevos Entornos y Lenguajes" in materias_aprobadas:
            mats_restantes -= 1
            horas_restantes -= 32

        # --- FASE 2: MATERIAS COMPARTIDAS (CORREGIDO) ---
        # Ahora recorremos directamente lo que el usuario tildó
        for m_nombre in materias_aprobadas:
            # La función aplicar_reglas ya tiene los ifs para saber si la materia cuenta o no
            mats_restantes, horas_restantes, aca_restante = aplicar_reglas_compartidas(
                m_nombre, carrera, plan, mats_restantes, horas_restantes, aca_restante
            )

        # --- CÁLCULO DE AVANCE FINAL ---
        total_puntos = row['total_horas'] + (row['req_total_creditos_aca'] * 10)
        puntos_faltantes = horas_restantes + (max(0, aca_restante) * 10)
        
        avance = round(((total_puntos - puntos_faltantes) / total_puntos) * 100, 1) if total_puntos > 0 else 0
        avance = max(0, min(100, avance))

        resultados.append({
            "Carrera": f"{carrera} ({plan})",
            "Avance (%)": avance,
            "Horas Faltantes": max(0, horas_restantes),
            "ACA Faltante": max(0, aca_restante),
            "Materias Restantes": max(0, mats_restantes)
        })

    return pd.DataFrame(resultados)