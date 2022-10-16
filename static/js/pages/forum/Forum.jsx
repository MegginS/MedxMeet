import React from "react";
import Topnavbar from "../../components/topnavbar/Topnavbar";
import Feed from "../../components/feed/Feed";
import Feedsidebar from "../../components/feedsidebar/Feedsidebar";
import "./newsfeed.css";

const Comment = () => {
  // this should display comment details and have buttons to edit or delete comment
  // editing or deleting a comment should refresh all comments
  return <></>;
};

const Post = () => {
  // this should display post details and have buttons to edit or delete post
  // editing or deleting a post should refresh all posts

  // maybe there could be a button to view comments
  // when view comments button is clicked, it fetches comments by post id from backend. It should be an array of Comments JSON
  // loop thru each comment to display each Comment component
  return <></>;
};

const ForumContainer = () => {
  // this should fetch Posts JSON by disease from backend. It should be an array of Posts JSON
  // loop through each Post to display each Post component
  return <></>;
};
