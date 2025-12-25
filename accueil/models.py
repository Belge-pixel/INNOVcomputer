from django.db import models


class Achievement(models.Model):
	CLIENT_SATISFIED = 'client_satisfait'
	PROJECT_COMPLETED = 'projet_realise'
	YEARS_EXPERIENCE = 'annee_d_experience'
	PARTNER_COMPANIES = 'entreprises_partenaires'

	ACHIEVEMENT_TYPE_CHOICES = [
		(CLIENT_SATISFIED, 'Client satisfait'),
		(PROJECT_COMPLETED, 'Projet réalisé'),
		(YEARS_EXPERIENCE, "Année d'expérience"),
		(PARTNER_COMPANIES, 'Entreprises partenaires'),
	]

	achievement_type = models.CharField(max_length=32, choices=ACHIEVEMENT_TYPE_CHOICES, unique=True)
	value = models.IntegerField(default=0)
	description = models.CharField(max_length=255, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = 'Achievement'
		verbose_name_plural = 'Achievements'

	def __str__(self):
		return f"{self.get_achievement_type_display()}: {self.value}"
