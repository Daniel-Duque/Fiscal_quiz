# -*- coding: utf-8 -*-
"""
Created on Tue Mar 11 06:08:45 2025

@author: usuario
"""

import streamlit as st

preguntas_respuestas_formato_lista = {
    "¿Qué autoridad municipal en Achí, Bolívar, evalúa los documentos para otorgar la exención del impuesto Predial Unificado?": {
        "respuestas": ["a) La Alcaldía Municipal", "b) El Concejo Municipal", "c) La Tesorería Municipal", "d) La Secretaría de Hacienda"],
        "correcta": "c) La Tesorería Municipal"
    },
    "Según el estatuto tributario de Achí, Bolívar, ¿qué implica cualquier incumplimiento de las condiciones exigidas para gozar de una exención?": {
        "respuestas": ["a) Una multa económica", "b) Un requerimiento especial", "c) La pérdida automática del beneficio", "d) Una prórroga para subsanar la falta"],
        "correcta": "c) La pérdida automática del beneficio"
    },
    "En Arcabuco, Boyacá, ¿ante qué oficina se puede solicitar la revisión del avalúo de un bien inmueble cuando se considera que no se ajusta a las características del predio?": {
        "respuestas": ["a) La Secretaría de Hacienda", "b) La Alcaldía Municipal", "c) La Oficina de Planeación Urbana", "d) La oficina de Catastro correspondiente"],
        "correcta": "d) La oficina de Catastro correspondiente"
    },
    "De acuerdo con el estatuto tributario de Arcabuco, Boyacá, cuando un propietario tiene varios predios, ¿bajo qué condición se le puede expedir un Certificado de Paz y Salvo por uno de esos predios?": {
        "respuestas": ["a) Si el impuesto del predio solicitado está al día", "b) Si cancela una cuota adicional", "c) Siempre y cuando se encuentre a paz y salvo por todo concepto", "d) Presentando una solicitud justificada"],
        "correcta": "c) Siempre y cuando se encuentre a paz y salvo por todo concepto"
    },
    "En Barranquilla, Atlántico, ¿qué tipo de declaración debe presentarse en casos de liquidación o terminación definitiva de actividades durante un período?": {
        "respuestas": ["a) Una declaración anual", "b) Una declaración bimestral", "c) Una declaración por la fracción del respectivo período", "d) Una declaración informativa"],
        "correcta": "c) Una declaración por la fracción del respectivo período"
    },
    "Según el decreto de Barranquilla, Atlántico, ¿cuál es el término para informar un cambio de dirección a la Administración Tributaria Distrital?": {
        "respuestas": ["a) Un mes", "b) Dos meses", "c) Tres meses", "d) Seis meses"],
        "correcta": "c) Tres meses"
    },
    "En Boavita, Boyacá, ¿quién debe enviar un requerimiento especial antes de efectuar una liquidación de revisión?": {
        "respuestas": ["a) El Alcalde Municipal", "b) El Concejo Municipal", "c) La Tesorería Municipal", "d) La Secretaría de Hacienda"],
        "correcta": "c) La Tesorería Municipal"
    },
    "De acuerdo con el estatuto tributario de Boavita, Boyacá, ¿cuál es el término máximo después de la fecha de presentación de la solicitud de devolución o compensación para que se notifique un requerimiento especial si la declaración presenta un saldo a favor?": {
        "respuestas": ["a) Un año", "b) Dos años", "c) Tres años", "d) Cinco años"],
        "correcta": "b) Dos años"
    },
    "En Campo de la Cruz, Atlántico, ¿cuál es el plazo máximo para pagar la primera cuota del impuesto de industria y comercio complementario de avisos y tableros para quienes opten por el pago en cuatro cuotas?": {
        "respuestas": ["a) El último día hábil del mes de Abril", "b) El último día hábil del mes de Mayo", "c) El último día hábil del mes de Marzo", "d) El último día hábil del mes de Junio"],
        "correcta": "c) El último día hábil del mes de Marzo"
    },
    "Según el estatuto tributario de Campo de la Cruz, Atlántico, ¿qué sanción se aplica por presentar las declaraciones tributarias de forma extemporánea?": {
        "respuestas": ["a) Un valor fijo en salarios mínimos", "b) Un porcentaje del patrimonio del declarante", "c) Un porcentaje del total del impuesto a cargo por cada mes de retardo", "d) La clausura del establecimiento"],
        "correcta": "c) Un porcentaje del total del impuesto a cargo por cada mes de retardo"
    },
    "En Arjona, Bolívar, ¿qué constituye plena prueba contra el contribuyente según el estatuto tributario municipal?": {
        "respuestas": ["a) El testimonio de terceros", "b) Una manifestación escrita del contribuyente informando un hecho que lo perjudica", "c) La presunción de ingresos por control de ventas", "d) El silencio del contribuyente ante un requerimiento verbal"],
        "correcta": "b) Una manifestación escrita del contribuyente informando un hecho que lo perjudica"
    },
    "De acuerdo con el estatuto tributario de Arjona, Bolívar, ¿cuál es el derecho por la expedición de un certificado de Paz y Salvo?": {
        "respuestas": ["a) 0,15 UVT", "b) 0,20 UVT", "c) 0,22 UVT", "d) 0,25 UVT"],
        "correcta": "c) 0,22 UVT"
    },
    "En Galapa, Atlántico, ¿ante quién debe interponerse el recurso de reconsideración contra los actos de la Administración Tributaria Municipal?": {
        "respuestas": ["a) El Alcalde Municipal", "b) El Concejo Municipal", "c) El mismo funcionario que dictó el acto", "d) La Secretaría de Gobierno"],
        "correcta": "c) El mismo funcionario que dictó el acto"
    },
    "Según el estatuto tributario de Galapa, Atlántico, ¿cuál es el plazo para interponer el recurso de reconsideración contado a partir de la notificación del acto?": {
        "respuestas": ["a) Un mes", "b) Dos meses", "c) Quince días", "d) Treinta días"],
        "correcta": "b) Dos meses"
    },
    "En Arbeláez, Cundinamarca, ¿cuál es el plazo mínimo para responder a requerimientos ordinarios o solicitudes de información por parte de la Secretaría de Hacienda?": {
        "respuestas": ["a) Cinco días calendario", "b) Diez días calendario", "c) Quince días calendario", "d) Veinte días calendario"],
        "correcta": "c) Quince días calendario"
    },
    "De acuerdo con el estatuto tributario de Arbeláez, Cundinamarca, ¿dentro de qué término deben los contribuyentes presentar sus libros de contabilidad si la solicitud de exhibición se efectúa por correo?": {
        "respuestas": ["a) Tres días siguientes a la notificación", "b) Cinco días siguientes a la notificación", "c) Ocho días siguientes a la notificación", "d) Diez días siguientes a la notificación"],
        "correcta": "c) Ocho días siguientes a la notificación"
    }
}

correctas=0
totales=0


for pregunta in preguntas_respuestas_formato_lista.keys():
    
    
    answer = st.radio(
        pregunta,preguntas_respuestas_formato_lista[pregunta]["respuestas"]
        ,

    )
    
    if answer == preguntas_respuestas_formato_lista[pregunta]["correcta"]:

        correctas+=1

    totales+=1
    
if st.button("finalizar", type="primary"):
    with st.chat_message("user"):
        st.write("tu resultado es:",str(100*correctas/totales))