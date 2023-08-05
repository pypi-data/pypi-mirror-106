from __future__ import annotations
from enum import Enum
from typing import Optional, Dict, List
from dataclasses import dataclass, field

@dataclass
class Document(object):
    '''Contexto para endpoints relacionadas a procedimentos clínicos(s)'''

    class Episode(object):
        '''Registro de episódio de transtorno ou doença'''
        class Start(str, Enum):
            '''episódio de início {}'''
            ACUTE = 'agudo'
            SUBACUTE = 'subagudo'
            INSIDIOUS = 'insidioso'
            INTERMITTENT = 'intermitente'

        class Intensity(str, Enum):
            '''de intensidade {}'''
            SEVERE = 'severa'
            MODERATE = 'moderada'
            MILD = 'leve'

        class Duration(str, Enum):
            '''com {} de duração'''
            MINUTES = 'minutos'
            HOURS = 'horas'
            DAYS = 'dias'
            WEEKS = 'semanas'
            MONTHS = 'meses'
            YEARS = 'anos'
            DECADES = 'décadas'

        class Presentation(str, Enum):
            ''', sendo a apresentação atual {}'''
            FIRST_EPISODE = 'o primeiro episódio'
            RECURRENT = 'recorrente'
            CONTINUOUS = 'crônica contínua'
            FLUCTUATING = 'crônica flutuante'
            IN_REMISSION = 'de remissão'

        start: Optional[Document.Episode.Start] = None
        intensity: Optional[Document.Episode.Intensity] = None
        duration: Optional[Document.Episode.Duration] = None
        presentation: Optional[Document.Episode.Presentation] = None
        notes: Optional[str] = None

        @staticmethod
        def render(
                start: Optional[ Document.Episode.Start ] = None,
                intensity: Optional[ Document.Episode.Intensity ] = None,
                duration: Optional[ Document.Episode.Duration ] = None,
                presentation: Optional[ Document.Episode.Presentation ] = None,
        ):
            OPTIONS: Dict[ str, str ] = {
                'start': 'O quadro teve início de forma {start}.',
                'intensity': 'O tratamento é considerado {efficacy} para controle da apresentação clínica.',
                'duration': 'Quando a eventos adversos reporta que a medicação é de forma geral {tolerability}.',
                'presentation': 'A medicação atual é {affordability} do ponto de vista financeiro.  Para controle da apresentação clínica é descrita como {efficacy}.',
                'affordability_tolerability': 'Quando a eventos adversos reporta que a medicação é de forma geral {}. Do ponto de vista financeiro é {affordability}.',
                'efficacy_tolerability': 'A medicação atual é {tolerability}, e quanto ao controle da apresentação clínica descrita como {efficacy}.',
                'affordability_efficacy_tolerability': 'A medicação atual é {efficacy} para controle da apresentação clínica. Do ponto de vista financeiro é {affordability}, e quanto a eventos adversos {tolerability}.',
            }

            if (start and intensity and duration and presentation):
                return OPTIONS[ 'start_intensity_duration_presentation' ].format(**dict(start=start, intensity=intensity, duration=duration, presentation=presentation))
            if (start and intensity and duration):
                return OPTIONS[ 'start_intensity_duration' ].format(**dict(start=start, intensity=intensity, duration=duration))
            if (start and intensity and presentation):
                return OPTIONS[ 'start_intensity_duration' ].format(**dict(start=start, intensity=intensity, presentation=presentation))
            if (start and presentation and duration):
                return OPTIONS[ 'start_intensity_duration' ].format(**dict(start=start, duration=duration, presentation=presentation))
            if (intensity and presentation and duration):
                return OPTIONS[ 'start_intensity_duration' ].format(**dict(start=start, duration=duration, presentation=presentation))
            else:
                return ''

    @dataclass
    class Visit(object):
        '''Registro de visita do paciente ao profissional'''

        class Type(str, Enum):
            '''{}.'''
            INITIAL = 'Visita Inicial'
            FOLLOW_UP = 'Visita de Seguimento'
            REVISION = 'Revisão de Tratamento'
            EMERGENCY = 'Visita de Emergência'

        class Reason(str, Enum):
            PHARMACOTHERAPY = 'Farmacoterapia'
            REPORT = 'Relatório'
            CERTIFICATE = 'Atestado'
            PSYCHOEDUCATION = 'Psicoeducação'
            PSYCHOTHERAPY = 'Psicoterapia'
            LABORATORY_CONTROL = 'Controle Laboratorial'

        main_complaint: Optional[ str ] = None


    class Report(object):

        class Type(str, Enum):
            '''Documento do tipo {}.'''
            MEDICAL_REPORT = 'Relatório Médico'
            MEDICAL_LICENCE = 'Licença Médica'
            TREATMENT_ATTENDANCE = 'Atestado de Comparecimento'

        class Informant(str, Enum):
            '''As informações foram fornecidas {}.'''
            PATIENT_ONLY = 'pelo paciente apenas'
            PATIENT_AND_RELATIVE = 'pelo paciente e acompanhante (familiar)'
            RELATIVE_ONLY = 'por familiar apenas'
            PATIENT_AND_OTHER = 'pelo paciente e acompanhante (terceiro)'
            OTHER_ONLY = 'por responsável (não familiar)'

        class Incapacity(str, Enum):
            '''A incapacidade atual é do tipo {}.'''
            TOTAL_PERMANENT = 'permanente e total'
            TOTAL_TEMPORARY = 'temporária porém total'
            PARTIAL_PERMANENT = 'parcial porém permanente'
            PARTIAL_TEMPORARY = 'parcial e temporária'

    class Pharmacotherapy(object):
        '''Em relação ao uso de medicações refere {}.'''

        class Efficacy(str, Enum):
            '''O tratamento é considerado {} para controle da apresentação clínica.'''
            EFFECTIVE = 'eficaz'
            MODERATE_EFFICACY = 'parcialmente eficaz'
            MILD_EFFICACY = 'pouco eficaz'
            INEFFECTIVE = 'ineficaz'

        class Tolerability(str, Enum):
            '''Quando a eventos adversos reporta que a medicação é de forma geral {}.'''
            TOLERABLE = 'bem tolerada'
            MODERATE_TOLERABILITY = 'parcialmente tolerada'
            MILD_TOLERABILITY = 'pouco tolerada'
            NOT_TOLERABLE = 'não tolerada'

        class Affordability(str, Enum):
            '''A medicação é {} do ponto de vista financeiro.'''
            AFFORDABLE = 'acessível'
            MODERATE_AFFORDABILITY = 'parcialmente acessível'
            MILD_AFFORDABILITY = 'pouco acessível'
            UNAFFORDABLE = 'inacessível'

        @staticmethod
        def get_pharmacotherapy(
                affordability: Optional[ Document.Pharmacotherapy.Affordability ] = None,
                efficacy: Optional[ Document.Pharmacotherapy.Efficacy ] = None,
                tolerability: Optional[ Document.Pharmacotherapy.Tolerability ] = None,
        ):
            OPTIONS: Dict[ str, str ] = {
                'affordability': 'A medicação é {affordability} do ponto de vista financeiro.',
                'efficacy': 'O tratamento é considerado {efficacy} para controle da apresentação clínica.',
                'tolerability': 'Quando a eventos adversos reporta que a medicação é de forma geral {tolerability}.',
                'affordability_efficacy': 'A medicação atual é {affordability} do ponto de vista financeiro.  Para controle da apresentação clínica é descrita como {efficacy}.',
                'affordability_tolerability': 'Quando a eventos adversos reporta que a medicação é de forma geral {}. Do ponto de vista financeiro é {affordability}.',
                'efficacy_tolerability': 'A medicação atual é {tolerability}, e quanto ao controle da apresentação clínica descrita como {efficacy}.',
                'affordability_efficacy_tolerability': 'A medicação atual é {efficacy} para controle da apresentação clínica. Do ponto de vista financeiro é {affordability}, e quanto a eventos adversos {tolerability}.',
            }

            if (efficacy and tolerability and affordability):
                return OPTIONS[ 'affordability_efficacy_tolerability' ].format(**dict(
                    efficacy=efficacy, tolerability=tolerability, affordability=affordability)
                                                                               )
            elif (affordability and efficacy):
                return OPTIONS[ 'affordability_efficacy' ].format(**dict(
                    efficacy=efficacy, affordability=affordability)
                                                                  )
            elif (affordability and tolerability):
                return OPTIONS[ 'affordability_tolerability' ].format(**dict(
                    tolerability=tolerability, affordability=affordability)
                                                                      )
            elif (efficacy and tolerability):
                return OPTIONS[ 'efficacy_tolerability' ].format(**dict(
                    tolerability=tolerability, efficacy=efficacy)
                                                                 )
            elif affordability:
                return OPTIONS['affordability'].format(affordability=affordability)

            elif efficacy:
                return OPTIONS['efficacy'].format(efficacy=efficacy)

            elif tolerability:
                return OPTIONS['tolerability'].format(tolerability=tolerability)

    # keys and references
    user_key: Optional[ str ] = None
    relation_key: Optional[ str ] = None
    report_key: Optional[ str ] = None
    prescription_key: Optional[ str ] = None
    visit_key: Optional[ str ] = None
    patient_key: Optional[ str ] = None
    professional_key: Optional[ str ] = None
    # professional
    professional_fullname: Optional[ str ] = None
    professional_profession: Optional[ str ] = None
    professional_licence: Optional[ str ] = None
    # patient
    patient_fullname: Optional[ str ] = None
    patient_birthdate: Optional[ str ] = None
    # exams results
    laboratory_result: Optional[ str ] = None
    image_result: Optional[ str ] = None
    other_exam_result: Optional[ str ] = None
    # external reports
    external_report: Optional[ str ] = None
    # clinical
    reason: Optional[ str ] = None
    current_medications: Optional[ str ] = None
    subjective: Optional[ str ] = None
    objective: Optional[ str ] = None
    assessment: Optional[ str ] = None
    plan: Optional[ str ] = None
    prescriptions: Optional[ str ] = None
    laboratory_recipe: Optional[ str ] = None
    image_recipe: Optional[ str ] = None
    # page content
    header: Optional[ str ] = None
    introduction: Optional[ str ] = None
    content: Optional[ str ] = None
    conclusion: Optional[ str ] = None
    created: Optional[ str ] = None

