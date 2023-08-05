from composer_hr.engine.enum import (Start, CurrentTherapy, CurrentIncapacity, CurrentState, EpisodeDuration, Evolution,
                                     VisitType, Reason, ReportType, MainInformant, PharmacotherapyAffordability,
                                     PharmacotherapyTolerability, PharmacotherapyEfficacy, ClinicalStability, DiseaseActivity)


if __name__ == '__main__':
    from composer_hr.engine.renderer import Render

    items = [
        ClinicalStability.STABLE,
        DiseaseActivity.INTERMITTENT,
        Start.ACUTE,
        Evolution.OSCILLATING,
        CurrentTherapy.REFUSE,
        CurrentState.MILD,
        PharmacotherapyEfficacy.EFFECTIVE,
        PharmacotherapyTolerability.MODERATE_TOLERABILITY,
        CurrentIncapacity.TOTAL_TEMPORARY,
        MainInformant.PATIENT_AND_OTHER,
        VisitType.FIRST_VISIT,
        Reason.DOCUMENTATION,

    ]

    print(Render(items)())
