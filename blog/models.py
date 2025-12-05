from django.db import models
from django.utils.text import slugify
from users.models import User


# ----------------------------------------------------------------
# 🔹 Modèle principal : New (Actualité / Article)
# ----------------------------------------------------------------
class New(models.Model):
    # Informations principales
    new_title = models.CharField(
        max_length=200,
        null=False,
        unique=True,
        verbose_name="Titre"
    )
    new_slug = models.SlugField(
        max_length=220,
        unique=True,
        blank=True,
        verbose_name="Slug"
    )
    new_content = models.TextField(verbose_name="Contenu")

    # Image associée à l’article
    new_image = models.ImageField(
        upload_to='blog_images/',
        blank=True,
        null=True,
        verbose_name="Image d’illustration"
    )

    # Auteur (lié à l’utilisateur)
    new_author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        default=None,
        related_name="news",
        verbose_name="Auteur"
    )

    # Dates
    new_publication_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Date de publication"
    )
    new_updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Dernière modification"
    )

    # Catégorie
    new_category = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Catégorie"
    )

    # Statut de publication
    STATUS_CHOICES = (
        ('draft', 'Brouillon'),
        ('published', 'Publié'),
    )
    new_status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='draft',
        verbose_name="Statut"
    )

    # Résumé / Extrait
    new_excerpt = models.TextField(
        max_length=300,
        blank=True,
        verbose_name="Résumé"
    )

    # Tags et statistiques
    new_tags = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="Mots-clés"
    )
    new_views = models.PositiveIntegerField(
        default=0,
        verbose_name="Nombre de vues"
    )

    class Meta:
        ordering = ['-new_publication_date']
        verbose_name = "Actualité"
        verbose_name_plural = "Actualités"

    def __str__(self):
        return self.new_title

    def save(self, *args, **kwargs):
        """
        Génère automatiquement un slug unique à partir du titre.
        Si le slug existe déjà, ajoute un suffixe numérique.
        """
        if not self.new_slug:
            base_slug = slugify(self.new_title)
            slug = base_slug
            counter = 1
            while New.objects.filter(new_slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.new_slug = slug
        super().save(*args, **kwargs)

    def short_content(self):
        """Retourne un extrait abrégé du contenu pour les aperçus."""
        if len(self.new_content) > 150:
            return f"{self.new_content[:150]}..."
        return self.new_content

    def tag_list(self):
        """Retourne la liste des tags séparés par virgules."""
        return [tag.strip() for tag in self.new_tags.split(',') if tag.strip()]


# ----------------------------------------------------------------
# 🔹 Modèle des commentaires
# ----------------------------------------------------------------
class Comment(models.Model):
    comment_content = models.TextField(verbose_name="Commentaire")
    comment_publication_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Date du commentaire"
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="Auteur du commentaire"
    )
    new = models.ForeignKey(
        New,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="Article concerné"
    )

    class Meta:
        ordering = ['-comment_publication_date']
        verbose_name = "Commentaire"
        verbose_name_plural = "Commentaires"

    def __str__(self):
        return f"Commentaire de {self.author} sur {self.new.new_title[:30]}"
