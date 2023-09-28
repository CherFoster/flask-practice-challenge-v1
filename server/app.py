from config import app, api
from models import Post, Comment
from flask_restful import Resource

# Create a GET route that goes to /api/sorted_posts. This route should return as json all the posts alphabetized by title.
class SortedPost(Resource):
  # sort by title
  def get(self):
    posts = Post.query.sort_by(Post.title).all()
    return (post.to_dict() for post in posts), 200
api.add_resource(SortedPost, '/api/sorted_posts', endpoint="sorted_posts")

# Create a GET route that goes to /api/posts_by_author/<author_name>. This route should return as json the post by the author's name. For example: /api/posts_by_author/sara would return all post that belong to sara.
class PostByAuthor(Resource):
  def get(self, author_name):
    post = Post.query.filter(Post.author == author_name).first()
    return post.to_dict(), 200
api.add_resource(PostByAuthor, "api/posts_by_author/<author_name>", endpoint="sorted_posts")

# Create a GET route that goes to /api/search_posts/<title>. This route should return as json all the posts that include the title. Capitalization shouldn't matter. So if you were to use this route like /api/search_posts/frog. It would give back all post that include frog in the title.
class SearchPosts(Resource):
    def get(self, title):
        titles = Post.query.filter(Post.title.ilike(f"%{title}%")).all()
        return [title.to_dict() for title in titles], 200
api.add_resource(SearchPosts, "/api/search_posts/<title>", endpoint="search_posts")

# Create a GET route that goes to /api/posts_ordered_by_comments. This route should return as json the posts ordered by how many comments the post contains in descendeding order. So the post with the most comments would show first all the way to the post with the least showing last.
class PostOrderedByComments(Resource):
   def get(self):
      postOrders = Post.query.sort_by(len(Post.comments)).desc().all()
      return [postOrder.to_dict() for postOrder in postOrders]
      
api.add_resource(PostOrderedByComments, '/api/posts_ordered_by_comments', endpoint='posts_ordered_by_comments')

# Create a GET route that goes to /api/most_popular_commenter. This route should return as json a dictionary like { commenter: "Bob" } of the commenter that's made the most comments. Since commenter isn't a model, think of how you can count the comments that has the same commenter name.
class MostPopularCommenter(Resource):
   def get(self):
      comments = Comment.query.all()
      commenters = [comment.commenter for comment in comments]

      


if __name__ == "__main__":
  app.run(port=5555, debug=True)