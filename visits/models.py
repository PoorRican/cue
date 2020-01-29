from django.db import models

from patients.models import Patient


class Visit(models.Model):
    NOT_EXAMINED = 'NE'
    EXAM_RESULTS = (('N', 'Normal'),
                    ('A', 'Abnormal'),
                    (NOT_EXAMINED, 'Not Examined'))
    date_in = models.fields.DateTimeField(auto_now_add=True)
    date_out = models.fields.DateTimeField(blank=True, null=True)

    patient = models.ForeignKey(Patient, related_name='visits', on_delete=models.PROTECT)

    description = models.fields.TextField()
    vaccinations = models.fields.CharField('Vaccines Administered', max_length=64, null=True, blank=True)
    fecal = models.fields.CharField(max_length=64, null=True, blank=True)

    # reasons for visit
    gen = models.fields.CharField('Gen. Appearance & Temp', max_length=2, choices=EXAM_RESULTS, default=NOT_EXAMINED)
    integumentary = models.fields.CharField(max_length=2, choices=EXAM_RESULTS, default=NOT_EXAMINED)
    eyes = models.fields.CharField(max_length=2, choices=EXAM_RESULTS, default=NOT_EXAMINED)
    ears = models.fields.CharField(max_length=2, choices=EXAM_RESULTS, default=NOT_EXAMINED)
    nose_throat = models.fields.CharField('Nose & Throat', max_length=2, choices=EXAM_RESULTS, default=NOT_EXAMINED)
    mm_teeth = models.fields.CharField('Mucous Membranes & Teeth', max_length=2, choices=EXAM_RESULTS,
                                       default=NOT_EXAMINED)
    musculoskeletal = models.fields.CharField(max_length=2, choices=EXAM_RESULTS, default=NOT_EXAMINED)
    circulatory = models.fields.CharField(max_length=2, choices=EXAM_RESULTS, default=NOT_EXAMINED)
    digestive = models.fields.CharField(max_length=2, choices=EXAM_RESULTS, default=NOT_EXAMINED)
    respiratory = models.fields.CharField(max_length=2, choices=EXAM_RESULTS, default=NOT_EXAMINED)
    genito_urinary = models.fields.CharField(max_length=2, choices=EXAM_RESULTS, default=NOT_EXAMINED)
    anal_sacs = models.fields.CharField(max_length=2, choices=EXAM_RESULTS, default=NOT_EXAMINED)
    neural_system = models.fields.CharField(max_length=2, choices=EXAM_RESULTS, default=NOT_EXAMINED)
    lymph_nodes = models.fields.CharField(max_length=2, choices=EXAM_RESULTS, default=NOT_EXAMINED)
    weight = models.fields.CharField(max_length=2, choices=EXAM_RESULTS, default=NOT_EXAMINED)
