from django.db import models
from django.db.models.fields import PositiveIntegerField
from mptt.models import MPTTModel, TreeForeignKey

class Process_bom(models.Model):
  title = models.CharField(max_length=1024)
  process_details = TreeForeignKey('Process_details',null=True,blank=True, on_delete=models.CASCADE)
  reqd_qty=models.FloatField()
  raw_material=models.PositiveIntegerField(default=0)
  job_order=models.PositiveIntegerField(default=0)
  slug = models.SlugField()

  def __str__(self):
    return self.title


class Process_details(MPTTModel):
  process_name=models.CharField(max_length=1024)
  parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True, on_delete=models.CASCADE)
  slug = models.SlugField(unique=True)

  class MPTTMeta:
    order_insertion_by = ['process_name']

  class Meta:
    unique_together = (('parent', 'slug',))
    verbose_name_plural = 'processdetails'

  def get_slug_list(self):
    try:
      ancestors = self.get_ancestors(include_self=True)
    except:
      ancestors = []
    else:
      ancestors = [ i.slug for i in ancestors]
    slugs = []
    for i in range(len(ancestors)):
      slugs.append('/'.join(ancestors[:i+1]))
    return slugs

  def __str__(self):
    return self.process_name