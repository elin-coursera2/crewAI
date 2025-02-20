from crewai.utilities.i18n import I18N
from crewai.utilities.llm_utils import create_llm

class Summarizer:
  i18n=I18N()
  llm=create_llm()

  def summarize(self, text: str) -> str:
    return self.llm.call(messages=[{
      'role': 'system',
      'content': self.i18n.slice('summarizer_system_message')
    }, {
      'role': 'user',
      'content': self.i18n.slice('summarize_instruction').format(group=text)
    }])
