from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from api.models import Charset
from api.models import Transcript
import regex as re
from api.models import User



def check_charset(value):
    charset = Charset.objects.get(id=1)
    regex = "["+charset.charset+"]+"
    matched = re.fullmatch(regex, value);
    if not bool(matched):
        raise serializers.ValidationError('Characters outside of the Character Set used. Only use characters present in the set.')
    return value

def check_only_one_or_zero_space(value):
    regex = "[\p{L}\-()',;:?.!]+( [\p{L}\-()',;:?.!]+)*"
    matched = re.fullmatch(regex, value)
    if not bool(matched):
        raise serializers.ValidationError("There can be only zero or one space between two characters")
    return value

def check_capital(value):
    regex = '((\p{Lu}|\p{Ll})((\p{Ll}+)|(\p{Lu}+)) ?)+'
    matched = re.fullmatch(regex, value)
    if not bool(matched):
        raise serializers.ValidationError("There can be only zero or one space between two characters")
    return value

def check_end_for_given_chars_or_for_an_uppercase_character(value):
    regex1 = ".* ?[\p{Lu}]$" #end with an upper case
    regex2 = ".*[?.!]$" #ends with [?.!]
    regex3 = ".*[,;:] ?$" #ends with [,;:] and then a space
    matched1 = re.fullmatch(regex1, value)
    matched2 = re.fullmatch(regex2, value)
    matched3 = re.fullmatch(regex3, value)
    if not bool(matched1) or not bool(matched2) or not bool(matched3):
        if (not bool(matched1) and not bool(matched2)) and not bool(matched3):
            raise serializers.ValidationError("characters ?.! should be end of text or followed by one space and an uppercase character")
        elif (bool(matched1) and bool(matched2)) and not bool(matched3):
            raise serializers.ValidationError("characters ,;: should be end of text or followed by one space")
    return value

class TranscriptSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    transcription = serializers.CharField(max_length=500,default='empty', validators=[check_charset, check_only_one_or_zero_space, check_end_for_given_chars_or_for_an_uppercase_character])
    audio = serializers.FilePathField(path='./media')
    transcribed = serializers.BooleanField(default=False)
    user = serializers.CharField(max_length=150, default=None)

    def create(self, validated_data):
        return Transcript.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.transcription = validated_data.get('transcription', instance.transcription)
        instance.audio = validated_data.get('audio', instance.audio)
        instance.transcribed = validated_data.get('transcribed', instance.transcribed)
        instance.user = validated_data.get('user', instance.user)
        instance.id = validated_data.get('id', instance.id)
        instance.save()
        return instance


    class Meta:
        model = Transcript
        fields = ('id','transcription', 'audio', 'transcribed', 'user')
