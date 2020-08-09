
### start test script
`./manage.py  test mobile_auth.tests.user --keepdb`


### Reference
```python
class FeedBackView(generics.CreateAPIView):
    queryset = FeedBack.objects.all()
    serializer_class = FeedBackSerializer
```

