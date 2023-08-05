from __future__ import print_function, unicode_literals
from rest_framework import status
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response


__all__ = [
  'BulkCreateModelMixin',
  'BulkDestroyModelMixin',
  'BulkUpdateModelMixin',
]


class BulkCreateModelMixin(CreateModelMixin):
  """
  Either create a single or many model instances in bulk by using the
  Serializers ``many=True`` ability from Django REST >= 2.2.5.

  .. note::
    This mixin uses the same method to create model instances
    as ``CreateModelMixin`` because both non-bulk and bulk
    requests will use ``POST`` request method.
  """

  def create(self, request, *args, **kwargs):
    bulk = isinstance(request.data, list)

    if not bulk:
      return super(BulkCreateModelMixin, self).create(request, *args, **kwargs)
    else:
      return_data = []
      # alex mooloo
      for list_el in request.data:
        serializer = self.get_serializer(data=list_el)
        serializer.is_valid(raise_exception=True)
        self.perform_bulk_create(serializer)
        return_data.append(serializer.data)
      return Response(return_data, status=status.HTTP_201_CREATED)

  def perform_bulk_create(self, serializer):
    return self.perform_create(serializer)


class BulkUpdateModelMixin(object):
  """
  Update model instances in bulk by using the Serializers
  ``many=True`` ability from Django REST >= 2.2.5.
  """

  def get_object(self):
    lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field

    if lookup_url_kwarg in self.kwargs:
      return super(BulkUpdateModelMixin, self).get_object()

    # If the lookup_url_kwarg is not present
    # get_object() is most likely called as part of options()
    # which by default simply checks for object permissions
    # and raises permission denied if necessary.
    # Here we don't need to check for general permissions
    # and can simply return None since general permissions
    # are checked in initial() which always gets executed
    # before any of the API actions (e.g. create, update, etc)
    return

  def perform_bulk_create(self, serializer):
    return self.perform_create(serializer)

  def bulk_update(self, request, *args, **kwargs):
    partial = kwargs.pop('partial', False)
    return_data = []
    i = 0
    # alex mooloo
    for list_el in request.data:
      if 'id' in list_el:
        obj = self.filter_queryset(self.get_queryset()).filter(pk=list_el['id']).first()
        if not obj:
          return Response("The object you are trying to update either does not exist or you do not have permission to update it", status=status.HTTP_403_FORBIDDEN)
        serializer = self.get_serializer(
          obj,
          data=list_el,
          partial=partial,
        )
      else:
        serializer = self.get_serializer(data=list_el)
      serializer.is_valid(raise_exception=True)
      if 'id' in list_el:
        self.perform_bulk_update(serializer)
      else:
        self.perform_bulk_create(serializer)
      return_data.append(serializer.data)
      i = i + 1
    return Response(return_data, status=status.HTTP_200_OK)

  def partial_bulk_update(self, request, *args, **kwargs):
    kwargs['partial'] = True
    return self.bulk_update(request, *args, **kwargs)

  def perform_update(self, serializer):
    serializer.save()

  def perform_bulk_update(self, serializer):
    return self.perform_update(serializer)


class BulkDestroyModelMixin(object):
  """
  Destroy model instances.
  """

  def allow_bulk_destroy(self, qs, filtered):
    """
    Hook to ensure that the bulk destroy should be allowed.

    By default this checks that the destroy is only applied to
    filtered querysets.
    """
    return qs is not filtered

  def bulk_destroy(self, request, *args, **kwargs):
    qs = self.get_queryset()

    filtered = self.filter_queryset(qs)
    if not self.allow_bulk_destroy(qs, filtered):
      return Response(status=status.HTTP_400_BAD_REQUEST)

    self.perform_bulk_destroy(filtered)

    return Response(status=status.HTTP_204_NO_CONTENT)

  def perform_destroy(self, instance):
    instance.delete()

  def perform_bulk_destroy(self, objects):
    for obj in objects:
      self.perform_destroy(obj)
