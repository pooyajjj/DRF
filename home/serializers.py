from rest_framework import serializers
from .models import Question, Answer


class PersonSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    age = serializers.IntegerField()
    email = serializers.EmailField()


class QuestionSerializer(serializers.ModelSerializer):
    answers = serializers.SerializerMethodField()
    user = serializers.StringRelatedField(read_only=True)


    class Meta:
        model = Question
        fields = '__all__'


    def get_answers(self,obj):
        result = obj.answer.all()
        return AnswerSerializer(instance=result, many=True).data



class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'