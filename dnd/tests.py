from pyvows import Vows, expect

from models import Character

@Vows.batch
class CharacterSpec(Vows.Context):
    def topic(self):
        return Character()

    def has_name(self, topic):
        expect(topic.name).to_equal('New Adventurer')

