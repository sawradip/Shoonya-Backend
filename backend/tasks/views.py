from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from tasks.models import Task, Annotation
from tasks.serializers import TaskSerializer, AnnotationSerializer

from users.models import User

# Create your views here.

class TaskViewSet(viewsets.ModelViewSet):
    """
        Model Viewset for Tasks. All Basic CRUD operations are covered here.
    """

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    @action(detail=True, methods=['post'], url_path='assign')
    def assign(self, request, pk):
        """
            Assigns users with the given user IDs to the particular task.
        """
        task = self.get_object()
        user_ids = request.data.get('user_ids')
        users = []
        for u_id in user_ids:
            try:
                users.append(User.objects.get(id=u_id))
            except User.DoesNotExist:
                return Response({"message": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        task.assign(users)
        return Response({"message": "Task assigned"}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['get'], url_path='annotations')
    def annotations(self, request, pk):
        """
            Returns all the annotations associated with a particular task.
        """
        task = self.get_object()
        annotations = Annotation.objects.filter(task=task)
        serializer = AnnotationSerializer(annotations, many=True)
        return Response(serializer.data)

        

class AnnotationViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    """
        Annotation Viewset with create and update operations.
    """
    queryset = Annotation.objects.all()
    serializer_class = AnnotationSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]