import dataclasses
import datetime
import enum
import typing
import markdown


class Render(object):
    '''Renderer text from enumeration instances, composing phrases and paragraphs for human reading.'''
    enums: typing.List[enum.Enum]
    text: bool = True
    html: bool = False
    markdown: bool = False
    _text: typing.ClassVar[str] = None
    _md: typing.ClassVar[str] = None
    _html: typing.ClassVar[str] = None
    _dict: typing.ClassVar[typing.Dict[str, enum.Enum]] = dict()

    def __init__(self, enums: typing.List[enum.Enum]):
        gen = (e for e in enums)
        _md, _text, _html = '', '', ''

        try:
            while True:
                item = next(gen)
                self._dict.update({item.__class__.__name__: item})
        except:
            if self._dict.get('VisitType'):
                _md += f'### {self._dict.get("VisitType")[0]}\n**{datetime.datetime.now().isoformat()}**\n\n---\n'
                _text += f'{self._dict.get("VisitType")[0]}: {datetime.datetime.now().isoformat()}.'

            if self._dict.get('ReportType'):
                _md += f'### {self._dict.get("ReportType")[0]}\n**{datetime.datetime.now().isoformat()}**\n\n---\n'
                _text += f'{self._dict.get("ReportType")[0]}: {datetime.datetime.now().isoformat()}.'

            _md += f'\n**INTRODUÇÃO.**\n'

            if self._dict.get('Reason'):
                _md += f'{self._dict.get("Reason").phrase}\n'
                _text += f'{self._dict.get("Reason").phrase} '

            if self._dict.get('MainInformant'):
                _md += f'{self._dict.get("MainInformant").phrase}\n'
                _text += f'{self._dict.get("MainInformant").phrase} '

            _md += f'\n**DADOS SUBJETIVOS.**\n'

            if self._dict.get('Start'):
                _md += f'{self._dict.get("Start").phrase}\n'
                _text += f'{self._dict.get("Start").phrase} '

            if self._dict.get('Evolution'):
                _md += f'{self._dict.get("Evolution").phrase}\n'
                _text += f'{self._dict.get("Evolution").phrase} '

            if self._dict.get('EpisodeDuration'):
                _md += f'{self._dict.get("EpisodeDuration").phrase}\n'
                _text += f'{self._dict.get("EpisodeDuration").phrase} '

            _md += f'\n**TRATAMENTO.**\n'

            if self._dict.get('PharmacotherapyEfficacy'):
                _md += f'{self._dict.get("PharmacotherapyEfficacy").phrase}\n'
                _text += f'{self._dict.get("PharmacotherapyEfficacy").phrase} '

            if self._dict.get('PharmacotherapyTolerability'):
                _md += f'{self._dict.get("PharmacotherapyTolerability").phrase}\n'
                _text += f'{self._dict.get("PharmacotherapyTolerability").phrase} '

            if self._dict.get('MedicationAdherence'):
                _md += f'{self._dict.get("MedicationAdherence").phrase}\n'
                _text += f'{self._dict.get("MedicationAdherence").phrase} '

            if self._dict.get('PharmacotherapyAffordability'):
                _md += f'{self._dict.get("PharmacotherapyAffordability").phrase}\n'
                _text += f'{self._dict.get("PharmacotherapyAffordability").phrase} '

            if self._dict.get('CurrentTherapy'):
                _md += f'{self._dict.get("CurrentTherapy").phrase}\n'
                _text += f'{self._dict.get("CurrentTherapy").phrase} '

            _md += f'\n**DISCUSSÃO.**\n'

            if self._dict.get('CurrentState'):
                _md += f'{self._dict.get("CurrentState").phrase}\n'
                _text += f'{self._dict.get("CurrentState").phrase} '

            if self._dict.get('ClinicalStability'):
                    _md += f'{self._dict.get("ClinicalStability").phrase}\n'
                    _text += f'{self._dict.get("ClinicalStability").phrase} '

            if self._dict.get('DiseaseActivity'):
                    _md += f'{self._dict.get("DiseaseActivity").phrase}\n'
                    _text += f'{self._dict.get("DiseaseActivity").phrase} '

            if self._dict.get('CurrentIncapacity'):
                _md += f'{self._dict.get("CurrentIncapacity").phrase}\n'
                _text += f'{self._dict.get("CurrentIncapacity").phrase} '

        finally:
            self._md = _md
            self._text = _text
            self._html = markdown.markdown(self._md)

    def __call__(self, *args, **kwargs):
        if kwargs.get('html'):
            return self._html.strip()
        elif kwargs.get('markdown'):
            return self._md.strip()
        return self._text.strip()